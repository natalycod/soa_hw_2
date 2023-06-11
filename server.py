
from concurrent import futures
import logging

import grpc
import mafia_pb2
import mafia_pb2_grpc
import threading
import queue

from typing import Iterable

current_sessions = {}

class Session:
    def __init__(self):
        self.session_name = ""
        self.users = []
        self.messages = []
        self.done_messages = 0

class MafiaConnection(mafia_pb2_grpc.MafiaServicer):
    def ConnectToServer(self, request, context):
        if request.session_name not in current_sessions:
            current_sessions[request.session_name] = Session()
        session = current_sessions[request.session_name]
        if request.user_name in session.users:
            yield mafia_pb2.ServerResponse(error=mafia_pb2.ServerResponse.ErrorMessage(error_type=mafia_pb2.ServerResponse.ErrorMessage.USER_EXISTS))
#            yield mafia_pb2.ConnectToServerResponse(success=False, error_message="User with name " + request.user_name + " already exists in session " + request.session_name)
        else:
            session.users.append(request.user_name)
            response = mafia_pb2.ServerResponse(new_connection=mafia_pb2.ServerResponse.NewConnectionMessage(new_user_name=request.user_name, current_users=session.users))
            yield response
#            yield mafia_pb2.ConnectToServerResponse(success=True)
            session.messages.append("User " + request.user_name + " connected to session\n")
        
#        while True:
#            while session.done_messages < len(session.messages):
#                yield mafia_pb2.ConnectToServerResponse(success=True, success_message=session.messages[session.done_messages])
#                session.done_messages += 1

port = "50051"
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
mafia_pb2_grpc.add_MafiaServicer_to_server(MafiaConnection(), server)
server.add_insecure_port("[::]:" + port)
server.start()
print("Server started, listening on " + port)
server.wait_for_termination()
