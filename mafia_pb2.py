# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mafia.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mafia.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bmafia.proto\"A\n\x16\x43onnectToServerMessage\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"Z\n\x17\x43onnectToServerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x17\n\x0fsuccess_message\x18\x03 \x01(\t\"0\n\x18GetConnectedUsersMessage\x12\x14\n\x0csession_name\x18\x01 \x01(\t\"/\n\x19GetConnectedUsersResponse\x12\x12\n\nuser_names\x18\x01 \x03(\t\"\xbf\x02\n\x0eServerResponse\x12-\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.ServerResponse.ErrorMessageH\x00\x12>\n\x0enew_connection\x18\x02 \x01(\x0b\x32$.ServerResponse.NewConnectionMessageH\x00\x1ah\n\x0c\x45rrorMessage\x12:\n\nerror_type\x18\x01 \x01(\x0e\x32&.ServerResponse.ErrorMessage.ErrorType\"\x1c\n\tErrorType\x12\x0f\n\x0bUSER_EXISTS\x10\x00\x1a\x44\n\x14NewConnectionMessage\x12\x15\n\rnew_user_name\x18\x01 \x01(\t\x12\x15\n\rcurrent_users\x18\x02 \x03(\tB\x0e\n\x0cmessage_type2\x96\x01\n\x05Mafia\x12?\n\x0f\x43onnectToServer\x12\x17.ConnectToServerMessage\x1a\x0f.ServerResponse\"\x00\x30\x01\x12L\n\x11GetConnectedUsers\x12\x19.GetConnectedUsersMessage\x1a\x1a.GetConnectedUsersResponse\"\x00\x62\x06proto3'
)



_SERVERRESPONSE_ERRORMESSAGE_ERRORTYPE = _descriptor.EnumDescriptor(
  name='ErrorType',
  full_name='ServerResponse.ErrorMessage.ErrorType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_EXISTS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=479,
  serialized_end=507,
)
_sym_db.RegisterEnumDescriptor(_SERVERRESPONSE_ERRORMESSAGE_ERRORTYPE)


_CONNECTTOSERVERMESSAGE = _descriptor.Descriptor(
  name='ConnectToServerMessage',
  full_name='ConnectToServerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_name', full_name='ConnectToServerMessage.session_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='ConnectToServerMessage.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=80,
)


_CONNECTTOSERVERRESPONSE = _descriptor.Descriptor(
  name='ConnectToServerResponse',
  full_name='ConnectToServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ConnectToServerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='ConnectToServerResponse.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success_message', full_name='ConnectToServerResponse.success_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=172,
)


_GETCONNECTEDUSERSMESSAGE = _descriptor.Descriptor(
  name='GetConnectedUsersMessage',
  full_name='GetConnectedUsersMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_name', full_name='GetConnectedUsersMessage.session_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=222,
)


_GETCONNECTEDUSERSRESPONSE = _descriptor.Descriptor(
  name='GetConnectedUsersResponse',
  full_name='GetConnectedUsersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_names', full_name='GetConnectedUsersResponse.user_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=271,
)


_SERVERRESPONSE_ERRORMESSAGE = _descriptor.Descriptor(
  name='ErrorMessage',
  full_name='ServerResponse.ErrorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_type', full_name='ServerResponse.ErrorMessage.error_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERRESPONSE_ERRORMESSAGE_ERRORTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=507,
)

_SERVERRESPONSE_NEWCONNECTIONMESSAGE = _descriptor.Descriptor(
  name='NewConnectionMessage',
  full_name='ServerResponse.NewConnectionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_user_name', full_name='ServerResponse.NewConnectionMessage.new_user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_users', full_name='ServerResponse.NewConnectionMessage.current_users', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=577,
)

_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='ServerResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_connection', full_name='ServerResponse.new_connection', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SERVERRESPONSE_ERRORMESSAGE, _SERVERRESPONSE_NEWCONNECTIONMESSAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message_type', full_name='ServerResponse.message_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=274,
  serialized_end=593,
)

_SERVERRESPONSE_ERRORMESSAGE.fields_by_name['error_type'].enum_type = _SERVERRESPONSE_ERRORMESSAGE_ERRORTYPE
_SERVERRESPONSE_ERRORMESSAGE.containing_type = _SERVERRESPONSE
_SERVERRESPONSE_ERRORMESSAGE_ERRORTYPE.containing_type = _SERVERRESPONSE_ERRORMESSAGE
_SERVERRESPONSE_NEWCONNECTIONMESSAGE.containing_type = _SERVERRESPONSE
_SERVERRESPONSE.fields_by_name['error'].message_type = _SERVERRESPONSE_ERRORMESSAGE
_SERVERRESPONSE.fields_by_name['new_connection'].message_type = _SERVERRESPONSE_NEWCONNECTIONMESSAGE
_SERVERRESPONSE.oneofs_by_name['message_type'].fields.append(
  _SERVERRESPONSE.fields_by_name['error'])
_SERVERRESPONSE.fields_by_name['error'].containing_oneof = _SERVERRESPONSE.oneofs_by_name['message_type']
_SERVERRESPONSE.oneofs_by_name['message_type'].fields.append(
  _SERVERRESPONSE.fields_by_name['new_connection'])
_SERVERRESPONSE.fields_by_name['new_connection'].containing_oneof = _SERVERRESPONSE.oneofs_by_name['message_type']
DESCRIPTOR.message_types_by_name['ConnectToServerMessage'] = _CONNECTTOSERVERMESSAGE
DESCRIPTOR.message_types_by_name['ConnectToServerResponse'] = _CONNECTTOSERVERRESPONSE
DESCRIPTOR.message_types_by_name['GetConnectedUsersMessage'] = _GETCONNECTEDUSERSMESSAGE
DESCRIPTOR.message_types_by_name['GetConnectedUsersResponse'] = _GETCONNECTEDUSERSRESPONSE
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConnectToServerMessage = _reflection.GeneratedProtocolMessageType('ConnectToServerMessage', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTTOSERVERMESSAGE,
  '__module__' : 'mafia_pb2'
  # @@protoc_insertion_point(class_scope:ConnectToServerMessage)
  })
_sym_db.RegisterMessage(ConnectToServerMessage)

ConnectToServerResponse = _reflection.GeneratedProtocolMessageType('ConnectToServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTTOSERVERRESPONSE,
  '__module__' : 'mafia_pb2'
  # @@protoc_insertion_point(class_scope:ConnectToServerResponse)
  })
_sym_db.RegisterMessage(ConnectToServerResponse)

GetConnectedUsersMessage = _reflection.GeneratedProtocolMessageType('GetConnectedUsersMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTEDUSERSMESSAGE,
  '__module__' : 'mafia_pb2'
  # @@protoc_insertion_point(class_scope:GetConnectedUsersMessage)
  })
_sym_db.RegisterMessage(GetConnectedUsersMessage)

GetConnectedUsersResponse = _reflection.GeneratedProtocolMessageType('GetConnectedUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTEDUSERSRESPONSE,
  '__module__' : 'mafia_pb2'
  # @@protoc_insertion_point(class_scope:GetConnectedUsersResponse)
  })
_sym_db.RegisterMessage(GetConnectedUsersResponse)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), {

  'ErrorMessage' : _reflection.GeneratedProtocolMessageType('ErrorMessage', (_message.Message,), {
    'DESCRIPTOR' : _SERVERRESPONSE_ERRORMESSAGE,
    '__module__' : 'mafia_pb2'
    # @@protoc_insertion_point(class_scope:ServerResponse.ErrorMessage)
    })
  ,

  'NewConnectionMessage' : _reflection.GeneratedProtocolMessageType('NewConnectionMessage', (_message.Message,), {
    'DESCRIPTOR' : _SERVERRESPONSE_NEWCONNECTIONMESSAGE,
    '__module__' : 'mafia_pb2'
    # @@protoc_insertion_point(class_scope:ServerResponse.NewConnectionMessage)
    })
  ,
  'DESCRIPTOR' : _SERVERRESPONSE,
  '__module__' : 'mafia_pb2'
  # @@protoc_insertion_point(class_scope:ServerResponse)
  })
_sym_db.RegisterMessage(ServerResponse)
_sym_db.RegisterMessage(ServerResponse.ErrorMessage)
_sym_db.RegisterMessage(ServerResponse.NewConnectionMessage)



_MAFIA = _descriptor.ServiceDescriptor(
  name='Mafia',
  full_name='Mafia',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=596,
  serialized_end=746,
  methods=[
  _descriptor.MethodDescriptor(
    name='ConnectToServer',
    full_name='Mafia.ConnectToServer',
    index=0,
    containing_service=None,
    input_type=_CONNECTTOSERVERMESSAGE,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetConnectedUsers',
    full_name='Mafia.GetConnectedUsers',
    index=1,
    containing_service=None,
    input_type=_GETCONNECTEDUSERSMESSAGE,
    output_type=_GETCONNECTEDUSERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAFIA)

DESCRIPTOR.services_by_name['Mafia'] = _MAFIA

# @@protoc_insertion_point(module_scope)