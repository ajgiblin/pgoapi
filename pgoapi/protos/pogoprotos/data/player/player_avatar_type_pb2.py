# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/player_avatar_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/player_avatar_type.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_pb=_b('\n/pogoprotos/data/player/player_avatar_type.proto\x12\x16pogoprotos.data.player*D\n\x10PlayerAvatarType\x12\x16\n\x12PLAYER_AVATAR_MALE\x10\x00\x12\x18\n\x14PLAYER_AVATAR_FEMALE\x10\x01\x62\x06proto3')
)

_PLAYERAVATARTYPE = _descriptor.EnumDescriptor(
  name='PlayerAvatarType',
  full_name='pogoprotos.data.player.PlayerAvatarType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLAYER_AVATAR_MALE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_AVATAR_FEMALE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=75,
  serialized_end=143,
)
_sym_db.RegisterEnumDescriptor(_PLAYERAVATARTYPE)

PlayerAvatarType = enum_type_wrapper.EnumTypeWrapper(_PLAYERAVATARTYPE)
PLAYER_AVATAR_MALE = 0
PLAYER_AVATAR_FEMALE = 1


DESCRIPTOR.enum_types_by_name['PlayerAvatarType'] = _PLAYERAVATARTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
