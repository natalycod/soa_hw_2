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
        self._queue = Queue()

        queue = Queue()
        threading.Thread(target=self.listen_for_messages, daemon=False, args=[]).start()
        threading.Thread(target=self.process_user_commands, daemon=False, args=[]).start()
        session_id = queue.get()

    def __exit__(self):
        self._stub.DisconnectFromServer(mafia_pb2.DisconnectToServerMessage(session_name=self.session_name, user_name=self.user_name))

    def listen_for_messages(self):
        self._stub.ConnectToServer(mafia_pb2.ConnectToServerMessage(session_name=self.session_name, user_name=self.user_name))

        while True:
            response = self._stub.GetNewMessage(mafia_pb2.GetMessageRequest(session_name=self.session_name, user_name=self.user_name))
            if response.HasField("success_connection"):
                print("You're successfully connected to the session!")
                print ("Current users: " + ", ".join(response.success_connection.current_users))
            if response.HasField("new_connection"):
                print("User " + response.new_connection.new_user_name + " connected to session")
                print("Current users: " + ", ".join(response.new_connection.current_users))
            if response.HasField("removed_connection"):
                print("User " + response.removed_connection.removed_user_name + " disconnected from session")
                print("Current users: " + ", ".join(response.removed_connection.current_users))
            if response.HasField("chat_message"):
                print(response.chat_message.user_name + ": " + response.chat_message.text)

    def process_user_commands(self):
        while True:
            command = input()
            if command.startswith("chat "):
                self._stub.SendUserCommand(mafia_pb2.SendUserCommandRequest(chat_message=mafia_pb2.SendUserCommandRequest.ChatMessage(session_name=self.session_name, user_name=self.user_name, text=command[5:])))

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
