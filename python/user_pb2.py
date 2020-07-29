# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nuser.proto\"\xa1\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x14\n\x0cmail_address\x18\x03 \x01(\t\x12!\n\tuser_type\x18\x04 \x01(\x0e\x32\x0e.User.UserType\"B\n\x08UserType\x12\n\n\x06NORMAL\x10\x00\x12\x11\n\rADMINISTRATOR\x10\x01\x12\t\n\x05GUEST\x10\x02\x12\x0c\n\x08\x44ISABLED\x10\x03\"\x19\n\x0bUserRequest\x12\n\n\x02id\x18\x01 \x01(\r\"C\n\x0cUserResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x04user\x18\x03 \x01(\x0b\x32\x05.User23\n\x0bUserManager\x12$\n\x03get\x12\x0c.UserRequest\x1a\r.UserResponse\"\x00\x62\x06proto3'
)



_USER_USERTYPE = _descriptor.EnumDescriptor(
  name='UserType',
  full_name='User.UserType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADMINISTRATOR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GUEST', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=110,
  serialized_end=176,
)
_sym_db.RegisterEnumDescriptor(_USER_USERTYPE)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='User.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='User.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mail_address', full_name='User.mail_address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='User.user_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USER_USERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=176,
)


_USERREQUEST = _descriptor.Descriptor(
  name='UserRequest',
  full_name='UserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=178,
  serialized_end=203,
)


_USERRESPONSE = _descriptor.Descriptor(
  name='UserResponse',
  full_name='UserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='UserResponse.error', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='UserResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='UserResponse.user', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=205,
  serialized_end=272,
)

_USER.fields_by_name['user_type'].enum_type = _USER_USERTYPE
_USER_USERTYPE.containing_type = _USER
_USERRESPONSE.fields_by_name['user'].message_type = _USER
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['UserRequest'] = _USERREQUEST
DESCRIPTOR.message_types_by_name['UserResponse'] = _USERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)

UserRequest = _reflection.GeneratedProtocolMessageType('UserRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UserRequest)
  })
_sym_db.RegisterMessage(UserRequest)

UserResponse = _reflection.GeneratedProtocolMessageType('UserResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERRESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UserResponse)
  })
_sym_db.RegisterMessage(UserResponse)



_USERMANAGER = _descriptor.ServiceDescriptor(
  name='UserManager',
  full_name='UserManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=274,
  serialized_end=325,
  methods=[
  _descriptor.MethodDescriptor(
    name='get',
    full_name='UserManager.get',
    index=0,
    containing_service=None,
    input_type=_USERREQUEST,
    output_type=_USERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERMANAGER)

DESCRIPTOR.services_by_name['UserManager'] = _USERMANAGER

# @@protoc_insertion_point(module_scope)