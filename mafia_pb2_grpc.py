# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mafia_pb2 as mafia__pb2


class MafiaStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConnectToServer = channel.unary_unary(
                '/Mafia/ConnectToServer',
                request_serializer=mafia__pb2.ConnectToServerMessage.SerializeToString,
                response_deserializer=mafia__pb2.CommonServerResponse.FromString,
                )
        self.GetNewMessage = channel.unary_unary(
                '/Mafia/GetNewMessage',
                request_serializer=mafia__pb2.GetMessageRequest.SerializeToString,
                response_deserializer=mafia__pb2.GetMessageResponse.FromString,
                )
        self.CheckUser = channel.unary_unary(
                '/Mafia/CheckUser',
                request_serializer=mafia__pb2.CheckUserRequest.SerializeToString,
                response_deserializer=mafia__pb2.CommonServerResponse.FromString,
                )
        self.KillUser = channel.unary_unary(
                '/Mafia/KillUser',
                request_serializer=mafia__pb2.KillUserRequest.SerializeToString,
                response_deserializer=mafia__pb2.CommonServerResponse.FromString,
                )
        self.SendChatMessage = channel.unary_unary(
                '/Mafia/SendChatMessage',
                request_serializer=mafia__pb2.SendChatMessageRequest.SerializeToString,
                response_deserializer=mafia__pb2.CommonServerResponse.FromString,
                )
        self.EndDay = channel.unary_unary(
                '/Mafia/EndDay',
                request_serializer=mafia__pb2.EndDayRequest.SerializeToString,
                response_deserializer=mafia__pb2.CommonServerResponse.FromString,
                )
        self.Publish = channel.unary_unary(
                '/Mafia/Publish',
                request_serializer=mafia__pb2.PublishRequest.SerializeToString,
                response_deserializer=mafia__pb2.CommonServerResponse.FromString,
                )
        self.Blame = channel.unary_unary(
                '/Mafia/Blame',
                request_serializer=mafia__pb2.BlameRequest.SerializeToString,
                response_deserializer=mafia__pb2.CommonServerResponse.FromString,
                )


class MafiaServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ConnectToServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNewMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KillUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendChatMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndDay(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Blame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MafiaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConnectToServer': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectToServer,
                    request_deserializer=mafia__pb2.ConnectToServerMessage.FromString,
                    response_serializer=mafia__pb2.CommonServerResponse.SerializeToString,
            ),
            'GetNewMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNewMessage,
                    request_deserializer=mafia__pb2.GetMessageRequest.FromString,
                    response_serializer=mafia__pb2.GetMessageResponse.SerializeToString,
            ),
            'CheckUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckUser,
                    request_deserializer=mafia__pb2.CheckUserRequest.FromString,
                    response_serializer=mafia__pb2.CommonServerResponse.SerializeToString,
            ),
            'KillUser': grpc.unary_unary_rpc_method_handler(
                    servicer.KillUser,
                    request_deserializer=mafia__pb2.KillUserRequest.FromString,
                    response_serializer=mafia__pb2.CommonServerResponse.SerializeToString,
            ),
            'SendChatMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendChatMessage,
                    request_deserializer=mafia__pb2.SendChatMessageRequest.FromString,
                    response_serializer=mafia__pb2.CommonServerResponse.SerializeToString,
            ),
            'EndDay': grpc.unary_unary_rpc_method_handler(
                    servicer.EndDay,
                    request_deserializer=mafia__pb2.EndDayRequest.FromString,
                    response_serializer=mafia__pb2.CommonServerResponse.SerializeToString,
            ),
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=mafia__pb2.PublishRequest.FromString,
                    response_serializer=mafia__pb2.CommonServerResponse.SerializeToString,
            ),
            'Blame': grpc.unary_unary_rpc_method_handler(
                    servicer.Blame,
                    request_deserializer=mafia__pb2.BlameRequest.FromString,
                    response_serializer=mafia__pb2.CommonServerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Mafia', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mafia(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ConnectToServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia/ConnectToServer',
            mafia__pb2.ConnectToServerMessage.SerializeToString,
            mafia__pb2.CommonServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNewMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia/GetNewMessage',
            mafia__pb2.GetMessageRequest.SerializeToString,
            mafia__pb2.GetMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia/CheckUser',
            mafia__pb2.CheckUserRequest.SerializeToString,
            mafia__pb2.CommonServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KillUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia/KillUser',
            mafia__pb2.KillUserRequest.SerializeToString,
            mafia__pb2.CommonServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendChatMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia/SendChatMessage',
            mafia__pb2.SendChatMessageRequest.SerializeToString,
            mafia__pb2.CommonServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EndDay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia/EndDay',
            mafia__pb2.EndDayRequest.SerializeToString,
            mafia__pb2.CommonServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia/Publish',
            mafia__pb2.PublishRequest.SerializeToString,
            mafia__pb2.CommonServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Blame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mafia/Blame',
            mafia__pb2.BlameRequest.SerializeToString,
            mafia__pb2.CommonServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
