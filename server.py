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
    
    def ConvertToGetMessageResponse(self):
        if self._type == MessageType.NONE:
            return mafia_pb2.GetMessageResponse(none_message=mafia_pb2.GetMessageResponse.NoneMessage())
        if self._type == MessageType.SUCCESS_CONNECTION:
            return mafia_pb2.GetMessageResponse(success_connection=mafia_pb2.GetMessageResponse.SuccessConnectionMessage(current_users=self.users))
        if self._type == MessageType.NEW_CONNECTION:
            return mafia_pb2.GetMessageResponse(new_connection=mafia_pb2.GetMessageResponse.NewConnectionMessage(new_user_name=self.user_name, current_users=self.users))

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
        self.users = []
    
    def add_user(self, user_name):
        self.users.append(User(user_name))
        for user in self.users:
            message = Message()
            if (user.name != user_name):
                message.make_new_connection_message(user_name, [user.name for user in self.users])
            else:
                message.make_success_connection_message([user.name for user in self.users])
            user.add_message(message)

    def get_users(self):
        return [user.name for user in self.users]
    
    def add_message_to_all_users(self, message):
        for user in self.users:
            user.add_message(message)
    
    def get_user_message(self, user_name):
        for user in self.users:
            if user.name == user_name:
                return user.get_message()

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
        result = []
        for user in current_sessions[request.session_name].users:
            result.append(user.name)
        return mafia_pb2.GetConnectedUsersResponse(user_names=result)

    def GetNewMessage(self, request, context):
        message = current_sessions[request.session_name].get_user_message(request.user_name)
        return message.ConvertToGetMessageResponse()

port = "50051"
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
mafia_pb2_grpc.add_MafiaServicer_to_server(MafiaConnection(), server)
server.add_insecure_port("[::]:" + port)
server.start()
print("Server started, listening on " + port)
server.wait_for_termination()
