from __future__ import print_function

import logging

import grpc
import mafia_pb2
import mafia_pb2_grpc
import threading
from typing import Iterator
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

class UserSession:
    def __init__(self, executor, channel, session_name, user_name):
        self.session_name = session_name
        self.user_name = user_name
        self.connected = False

        self._executor = executor
        self._channel = channel
        self._consumer_future = None
        self._stub = mafia_pb2_grpc.MafiaStub(self._channel)

        queue = Queue()
        threading.Thread(target=self.listen_for_messages, daemon=False, args=[]).start()

        session_id = queue.get()

    def listen_for_messages(self):
        responses = self._stub.ConnectToServer(mafia_pb2.ConnectToServerMessage(session_name=self.session_name, user_name=self.user_name))
        for response in responses:
            if response.HasField("new_connection"):
                print("User " + response.new_connection.new_user_name + " connected to session")
                print("Current users: ", response.new_connection.current_users)
            elif response.HasField("error"):
                if response.error.error_type == mafia_pb2.ServerResponse.ErrorMessage.USER_EXISTS:
                    print("User with this name already exists")

print("Hi! Wanna play some mafia?")
print("Enter name of session you want to connect to")
session_name = input()
print("Enter your username")
user_name = input()


with grpc.insecure_channel("localhost:50051") as channel:
    executor = ThreadPoolExecutor()
    user_session = UserSession(executor, channel, session_name, user_name)

while True:
    pass