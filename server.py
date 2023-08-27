from concurrent import futures

import grpc
import mafia_pb2
import mafia_pb2_grpc
import random

from queue import Queue
from enum import Enum

current_sessions = {}

class MessageType(Enum):
    NONE = 1
    SUCCESS_CONNECTION = 2
    NEW_CONNECTION = 3
    REMOVED_CONNECTION = 4
    CHAT_MESSAGE = 5
    NEW_ROLE_MESSAGE = 6
    NEW_GAME_STAGE = 7

class Message:
    def __init__(self):
        self._type = MessageType.NONE

    def make_new_connection_message(self, user_name, users):
        self._type = MessageType.NEW_CONNECTION
        self.user_name = user_name
        self.users = users
    
    def make_success_connection_message(self, users):
        self._type = MessageType.SUCCESS_CONNECTION
        self.users = users
    
    def make_removed_connection_message(self, user_name, users):
        self._type = MessageType.REMOVED_CONNECTION
        self.user_name = user_name
        self.users = users
    
    def make_user_chat_message(self, user_name, text):
        self._type = MessageType.CHAT_MESSAGE
        self.user_name = user_name
        self.text = text
    
    def make_new_role_message(self, role_name):
        self._type = MessageType.NEW_ROLE_MESSAGE
        self.role_name = role_name
    
    def make_new_game_stage(self, stage_name):
        self._type = MessageType.NEW_GAME_STAGE
        self.stage_name = stage_name

    def ConvertToGetMessageResponse(self):
        if self._type == MessageType.NONE:
            return mafia_pb2.GetMessageResponse(none_message=mafia_pb2.GetMessageResponse.NoneMessage())
        if self._type == MessageType.SUCCESS_CONNECTION:
            return mafia_pb2.GetMessageResponse(success_connection=mafia_pb2.GetMessageResponse.SuccessConnectionMessage(current_users=self.users))
        if self._type == MessageType.NEW_CONNECTION:
            return mafia_pb2.GetMessageResponse(new_connection=mafia_pb2.GetMessageResponse.NewConnectionMessage(new_user_name=self.user_name, current_users=self.users))
        if self._type == MessageType.REMOVED_CONNECTION:
            return mafia_pb2.GetMessageResponse(removed_connection=mafia_pb2.GetMessageResponse.RemovedConnectionMessage(removed_user_name=self.user_name, current_users=self.users))
        if self._type == MessageType.CHAT_MESSAGE:
            return mafia_pb2.GetMessageResponse(chat_message=mafia_pb2.GetMessageResponse.ChatMessage(user_name=self.user_name, text=self.text))
        if self._type == MessageType.NEW_ROLE_MESSAGE:
            return mafia_pb2.GetMessageResponse(new_role_message=mafia_pb2.GetMessageResponse.NewRoleMessage(role_name=self.role_name))
        if self._type == MessageType.NEW_GAME_STAGE:
            return mafia_pb2.GetMessageResponse(new_stage_message=mafia_pb2.GetMessageResponse.NewStageMessage(stage_name=self.stage_name))

class Role(Enum):
    NONE = 'none'
    PEACEFUL = 'peaceful'
    MAFIA = 'mafia'
    COMISSAR = 'comissar'

class GameStage(Enum):
    NOT_STARTED = 'not_started'
    DAY = 'day'
    NIGHT = 'night'

class User:
    def __init__(self, name):
        self.name = name
        self.role = Role.NONE
        self.messages = Queue()
        self.ready_to_end_day = False
    
    def add_message(self, message):
        self.messages.put(message)
    
    def get_message(self):
        if self.messages.empty():
            return Message()
        return self.messages.get()

    def set_role(self, user_role):
        self.role = user_role
        message = Message()
        message.make_new_role_message(self.role.value)
        self.add_message(message)

class Session:
    def __init__(self):
        self.session_name = ""
        self.game_stage = GameStage.NOT_STARTED
        self.users = {}
        self.ready_to_end_day_count = 0
    
    def add_user(self, user_name):
        self.users[user_name] = User(user_name)
        for name, user in self.users.items():
            message = Message()
            if (name != user_name):
                message.make_new_connection_message(user_name, [_name for _name, _user in self.users.items()])
            else:
                message.make_success_connection_message([_name for _name, _user in self.users.items()])
            user.add_message(message)
        if len(self.users) >= 2:
            self.start_game()
    
    def remove_user(self, user_name):
        self.users.pop(user_name)
        for name, user in self.users.items():
            message = Message()
            message.make_lost_connection_message(user_name, [_name for _name, _user in self.users.items()])

    def get_user_message(self, user_name):
        if user_name not in self.users:
            return Message()
        return self.users[user_name].get_message()

    def send_user_message(self, user_name, text):
        message = Message()
        message.make_user_chat_message(user_name, text)
        for name, user in self.users.items():
            user.add_message(message)
    
    def start_game(self):
        self.game_stage = GameStage.DAY
        current_users = [_name for _name, _user in self.users.items()]
        random.shuffle(current_users)
        self.users[current_users[0]].set_role(Role.COMISSAR)
        self.users[current_users[1]].set_role(Role.MAFIA)
        for i in range(2, len(current_users)):
            self.users[current_users[i]].set_role(Role.PEACEFUL)
    
    def end_day(self, user_name):
        if user_name not in self.users:
            return
        if not self.users[user_name].ready_to_end_day:
            self.ready_to_end_day_count += 1
            self.users[user_name].ready_to_end_day = True
        if self.ready_to_end_day_count == len(self.users):
            print("night")
            self.game_stage = GameStage.NIGHT
            self.ready_to_end_day_count = 0
            for name, user in self.users.items():
                user.ready_to_end_day = False
                message = Message()
                message.make_new_game_stage(self.game_stage.value)
                user.add_message(message)

class MafiaConnection(mafia_pb2_grpc.MafiaServicer):
    def ConnectToServer(self, request, context):
        if request.session_name not in current_sessions:
            current_sessions[request.session_name] = Session()
        session = current_sessions[request.session_name]
        if request.user_name in current_sessions[request.session_name].users:
            return mafia_pb2.CommonServerResponse(common_error=mafia_pb2.CommonServerResponse.CommonError(error_text="User with name " + request.user_name + " already exists in session " + request.session_name))
        if current_sessions[request.session_name].game_stage != GameStage.NOT_STARTED:
            return mafia_pb2.CommonServerResponse(common_error=mafia_pb2.CommonServerResponse.CommonError(error_text="Session " + request.session_name + " already started, you can't connect to it."))

        session.add_user(request.user_name)
        return mafia_pb2.CommonServerResponse(empty_message=mafia_pb2.CommonServerResponse.EmptyMessage())

    def DisconnectFromServer(self, request, context):
        current_sessions[request.session_name].remove_user(request.user_name)
        mafia_pb2.CommonServerResponse(empty_message=mafia_pb2.CommonServerResponse.EmptyMessage())

    def GetNewMessage(self, request, context):
        message = current_sessions[request.session_name].get_user_message(request.user_name)
        return message.ConvertToGetMessageResponse()

    def SendUserCommand(self, request, context):
        if request.HasField("chat_message"):
            if current_sessions[request.chat_message.session_name].game_stage == GameStage.NIGHT:
                return mafia_pb2.CommonServerResponse(common_error=mafia_pb2.CommonServerResponse.CommonError(error_text="You can't use chat at night"))
            current_sessions[request.chat_message.session_name].send_user_message(request.chat_message.user_name, request.chat_message.text)
            return mafia_pb2.CommonServerResponse(empty_message=mafia_pb2.CommonServerResponse.EmptyMessage())
        if request.HasField("end_day"):
            if current_sessions[request.end_day.session_name].game_stage != GameStage.DAY:
                return mafia_pb2.CommonServerResponse(common_error=mafia_pb2.CommonServerResponse.CommonError(error_text="You can't end day, because it's not day now"))
            current_sessions[request.end_day.session_name].end_day(request.end_day.user_name)
            return mafia_pb2.CommonServerResponse(empty_message=mafia_pb2.CommonServerResponse.EmptyMessage())

port = "50051"
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
mafia_pb2_grpc.add_MafiaServicer_to_server(MafiaConnection(), server)
server.add_insecure_port("[::]:" + port)
server.start()
print("Server started, listening on " + port)
server.wait_for_termination()
