from concurrent import futures

import grpc
import mafia_pb2
import mafia_pb2_grpc
import random
import threading

from queue import Queue
from enum import Enum

current_sessions = {}

class MessageType(Enum):
    NONE = 1
    SERVER_MESSAGE = 2
    USER_MESSAGE = 3

class Message:
    def __init__(self):
        self._type = MessageType.NONE

    def make_server_message(self, text, is_major_type):
        self._type = MessageType.SERVER_MESSAGE
        self.text = text
        self.major_type = is_major_type
    
    def make_user_message(self, user_name, text, is_major_type):
        self._type = MessageType.USER_MESSAGE
        self.user_name = user_name
        self.text = text
        self.major_type = is_major_type

    def ConvertToGetMessageResponse(self):
        if self._type == MessageType.NONE:
            return mafia_pb2.GetMessageResponse(none_message=mafia_pb2.GetMessageResponse.NoneMessage())
        if self._type == MessageType.SERVER_MESSAGE:
            return mafia_pb2.GetMessageResponse(server_message=mafia_pb2.GetMessageResponse.ServerMessage(text=self.text, major_type=self.major_type))
        if self._type == MessageType.USER_MESSAGE:
            return mafia_pb2.GetMessageResponse(user_message=mafia_pb2.GetMessageResponse.UserMessage(user_name=self.user_name, text=self.text, major_type=self.major_type))

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
        self.ready_to_end_night = False
        self.alive = True
    
    def add_message(self, message):
        self.messages.put(message)
    
    def get_message(self):
        if self.messages.empty():
            return Message()
        return self.messages.get()

    def set_role(self, user_role):
        self.role = user_role
        message = Message()
        message.make_server_message("Your role is " + self.role.value, False)
        self.add_message(message)

class Session:
    def __init__(self):
        self.session_name = ""
        self.game_stage = GameStage.NOT_STARTED
        self.users = {}
        self.ready_to_end_day_count = 0
        self.ready_to_end_night_count = 0

        threading.Thread(target=self._keep_relevant, daemon=False, args=[]).start()

    def _try_to_start_game(self):
        if len(self.users) < 2:
            return False
        self.game_stage = GameStage.DAY
        self.ready_to_end_day_count = 0
        self.ready_to_end_night_count = 0
        for name, user in self.users.items():
            user.ready_to_end_day = False
            user.ready_to_end_night = False
            if not user.alive:
                user.ready_to_end_day = True
                user.ready_to_end_night = True
                self.ready_to_end_day_count += 1
                self.ready_to_end_night_count += 1
            elif user.role == Role.PEACEFUL:
                user.ready_to_end_night = True
                self.ready_to_end_night_count += 1
            message = Message()
            message.make_server_message("--- GAME STARTED ---", True)
            user.add_message(message)

        current_users = [_name for _name, _user in self.users.items()]
        random.shuffle(current_users)
        self.users[current_users[0]].set_role(Role.COMISSAR)
        self.users[current_users[1]].set_role(Role.MAFIA)
        for i in range(2, len(current_users)):
            self.users[current_users[i]].set_role(Role.PEACEFUL)
        return True

    def _try_to_end_day(self):
        if self.ready_to_end_day_count < len(self.users):
            return False
        self.game_stage = GameStage.NIGHT
        self.ready_to_end_day_count = 0
        self.ready_to_end_night_count = 0
        for name, user in self.users.items():
            user.ready_to_end_day = False
            user.ready_to_end_night = False
            if not user.alive:
                user.ready_to_end_day = True
                user.ready_to_end_night = True
                self.ready_to_end_day_count += 1
                self.ready_to_end_night_count += 1
            elif user.role == Role.PEACEFUL:
                user.ready_to_end_night = True
                self.ready_to_end_night_count += 1
            message = Message()
            message.make_server_message("--- NIGHT TIME ---", True)
            user.add_message(message)
        return True

    def _try_to_end_night(self):
        if self.ready_to_end_night_count < len(self.users):
            return False
        self.game_stage = GameStage.DAY
        self.ready_to_end_day_count = 0
        self.ready_to_end_night_count = 0
        for name, user in self.users.items():
            user.ready_to_end_day = False
            user.ready_to_end_night = False
            if not user.alive:
                user.ready_to_end_day = True
                user.ready_to_end_night = True
                self.ready_to_end_day_count += 1
                self.ready_to_end_night_count += 1
            elif user.role == Role.PEACEFUL:
                user.ready_to_end_night = True
                self.ready_to_end_night_count += 1
            message = Message()
            message.make_server_message("--- DAY TIME ---", True)
            user.add_message(message)
        return True

    def _try_to_end_game(self):
        pass

    def _keep_relevant(self):
        while True:
            self._try_to_end_game()
            if self.game_stage == GameStage.NOT_STARTED:
                self._try_to_start_game()
            if self.game_stage == GameStage.DAY:
                self._try_to_end_day()
            elif self.game_stage == GameStage.NIGHT:
                self._try_to_end_night()

    def add_user(self, user_name):
        self.users[user_name] = User(user_name)
        for name, user in self.users.items():
            connection_message = Message()
            current_users_message = Message()
            if (name == user_name):
                connection_message.make_server_message("You were succesfully connected!", False)
            else:
                connection_message.make_server_message("User " + user_name + " joined the session", True)
            current_users_message.make_server_message("Current users: " + ", ".join([_name for _name, _user in self.users.items()]), True)
            user.add_message(connection_message)
            user.add_message(current_users_message)

    def get_user_message(self, user_name):
        if user_name not in self.users:
            return Message()
        return self.users[user_name].get_message()

    def send_user_message(self, user_name, text):
        for name, user in self.users.items():
            message = Message()
            if name == user_name:
                message.make_user_message(user_name, text, True)
            else:
                message.make_user_message(user_name, text, False)
            user.add_message(message)
    
    def get_alive_players(self):
        result = []
        for name, user in self.users.items():
            if user.alive:
                result.append(name)
        return result

    def end_day(self, user_name):
        if user_name not in self.users:
            return
        if not self.users[user_name].ready_to_end_day:
            self.ready_to_end_day_count += 1
            self.users[user_name].ready_to_end_day = True
    
    def process_victim(self, user_name, victim_name):
        if self.users[user_name].ready_to_end_night:
            return []
        self.users[user_name].ready_to_end_night = True
        self.ready_to_end_night_count += 1

        if self.users[user_name].role == Role.MAFIA:
            self.users[victim_name].alive = False
            return [Role.MAFIA]
        if self.users[user_name].role == Role.COMISSAR:
            if self.users[victim_name].role == Role.MAFIA:
                return [Role.COMISSAR, True]
            else:
                return [Role.COMISSAR, False]
        return []

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
    
    def GetAlivePlayers(self, request, context):
        return mafia_pb2.GetAlivePlayersResponse(players=current_sessions[request.session_name].get_alive_players())

    def SendVictimName(self, request, context):
        resp = current_sessions[request.session_name].process_victim(request.user_name, request.victim_name)
        if len(resp) == 0:
            return mafia_pb2.SendVictimNameResponse(already_chose=mafia_pb2.SendVictimNameResponse.AlreadyChoseResponse())
        if resp[0] == Role.MAFIA:
            return mafia_pb2.SendVictimNameResponse(mafia_response=mafia_pb2.SendVictimNameResponse.MafiaResponse(chosen_victim=request.victim_name))
        elif resp[0] == Role.COMISSAR:
            return mafia_pb2.SendVictimNameResponse(comissar_response=mafia_pb2.SendVictimNameResponse.ComissarResponse(chosen_victim=request.victim_name, is_mafia=resp[1]))


port = "50051"
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
mafia_pb2_grpc.add_MafiaServicer_to_server(MafiaConnection(), server)
server.add_insecure_port("[::]:" + port)
server.start()
print("Server started, listening on " + port)
server.wait_for_termination()
