from concurrent import futures

import grpc
import mafia_pb2
import mafia_pb2_grpc

from typing import Iterable
from queue import Queue
from enum import Enum

current_sessions = {}

class MessageType(Enum):
    NONE = 1
    SUCCESS_CONNECTION = 2
    NEW_CONNECTION = 3
    REMOVED_CONNECTION = 4
    CHAT_MESSAGE = 5

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

class Role(Enum):
    PEACEFUL = 1
    MAFIA = 2
    COMISSAR = 3

class GameStage(Enum):
    NOT_STARTED = 1
    DAY = 2
    NIGHT = 3

class User:
    def __init__(self, name):
        self.name = name
        self.messages = Queue()
    
    def add_message(self, message):
        self.messages.put(message)
    
    def get_message(self):
        if self.messages.empty():
            return Message()
        return self.messages.get()

class Session:
    def __init__(self):
        self.session_name = ""
        self.game_stage = GameStage.NOT_STARTED
        self.users = {}
    
    def add_user(self, user_name):
        self.users[user_name] = User(user_name)
        for name, user in self.users.items():
            message = Message()
            if (name != user_name):
                message.make_new_connection_message(user_name, [_name for _name, _user in self.users.items()])
            else:
                message.make_success_connection_message([_name for _name, _user in self.users.items()])
            user.add_message(message)
    
    def remove_user(self, user_name):
        self.users.pop(user_name)
        for name, user in self.users.items():
            message = Message()
            message.make_lost_connection_message(user_name, [_name for _name, _user in self.users.items()])

    def get_user_message(self, user_name):
        return self.users[user_name].get_message()

    def send_user_message(self, user_name, text):
        message = Message()
        message.make_user_chat_message(user_name, text)
        for name, user in self.users.items():
            user.add_message(message)

class MafiaConnection(mafia_pb2_grpc.MafiaServicer):
    def ConnectToServer(self, request, context):
        if request.session_name not in current_sessions:
            current_sessions[request.session_name] = Session()
        session = current_sessions[request.session_name]
        if request.user_name in []:
            return mafia_pb2.EmptyServerResponse()
        else:
            session.add_user(request.user_name)
            response = mafia_pb2.EmptyServerResponse()
            return response

    def GetConnectedUsers(self, request, context):
        result = [_name for _name, _users in current_sessions[request.session_name].users.items()]
        return mafia_pb2.GetConnectedUsersResponse(user_names=result)

    def GetNewMessage(self, request, context):
        message = current_sessions[request.session_name].get_user_message(request.user_name)
        return message.ConvertToGetMessageResponse()

    def SendUserCommand(self, request, context):
        if request.HasField("chat_message"):
            current_sessions[request.chat_message.session_name].send_user_message(request.chat_message.user_name, request.chat_message.text)
            return mafia_pb2.EmptyServerResponse()

port = "50051"
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
mafia_pb2_grpc.add_MafiaServicer_to_server(MafiaConnection(), server)
server.add_insecure_port("[::]:" + port)
server.start()
print("Server started, listening on " + port)
server.wait_for_termination()
