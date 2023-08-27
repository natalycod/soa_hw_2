from __future__ import print_function

import logging

import grpc
import mafia_pb2
import mafia_pb2_grpc
import threading
from typing import Iterator
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

    def listen_for_messages(self):
        response = self._stub.ConnectToServer(mafia_pb2.ConnectToServerMessage(session_name=self.session_name, user_name=self.user_name))
        if response.HasField("common_error"):
            print("error: " + response.common_error.error_text)
        
        while True:
            response = self._stub.GetNewMessage(mafia_pb2.GetMessageRequest(session_name=self.session_name, user_name=self.user_name))
            if response.HasField("server_message"):
                if response.server_message.major_type:
                    print(bcolors.OKBLUE + response.server_message.text + bcolors.ENDC)
                else:
                    print(bcolors.OKCYAN + response.server_message.text + bcolors.ENDC)
            if response.HasField("user_message"):
                if response.user_message.major_type:
                    print(bcolors.BOLD + bcolors.OKGREEN + response.user_message.user_name + ": " + response.user_message.text + bcolors.ENDC + bcolors.ENDC)
                else:
                    print(bcolors.OKGREEN + response.user_message.user_name + ": " + response.user_message.text + bcolors.ENDC)

    def process_user_commands(self):
        while True:
            command = input()
            if command.startswith("chat "):
                response = self._stub.SendUserCommand(mafia_pb2.SendUserCommandRequest(chat_message=mafia_pb2.SendUserCommandRequest.ChatMessage(session_name=self.session_name, user_name=self.user_name, text=command[5:])))
                if response.HasField("common_error"):
                    print("error: " + response.common_error.error_text)
            if command.startswith("end_day"):
                response = self._stub.SendUserCommand(mafia_pb2.SendUserCommandRequest(end_day=mafia_pb2.SendUserCommandRequest.EndDayMessage(session_name=self.session_name, user_name=self.user_name)))
                if response.HasField("common_error"):
                    print("error: " + response.common_error.error_text)
            if command.startswith("victim "):
                response = self._stub.SendVictimName(mafia_pb2.SendVictimNameRequest(session_name=self.session_name, user_name=self.user_name, victim_name=command[7:]))
                if response.HasField("comissar_response"):
                    if response.comissar_response.is_mafia:
                        print("Congratulations! " + response.comissar_response.chosen_victim + " is mafia!")
                    else:
                        print("Sorry, " + response.comissar_response.chosen_victim + " is not mafia. Try again next night.")
                if response.HasField("mafia_response"):
                    print("Fine, you can consider " + response.mafia_response.chosen_victim + " dead.")
                if response.HasField("already_chose"):
                    print("You already chose your victim. Try again next night.")

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
