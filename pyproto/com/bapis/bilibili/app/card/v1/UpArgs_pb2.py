# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.card.v1.UpArgs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.card.v1.UpArgs.proto',
  package='com.bapis.bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3pyproto/com.bapis.bilibili.app.card.v1.UpArgs.proto\x12\x1e\x63om.bapis.bilibili.app.card.v1\"\x8e\x01\n\x06UpArgs\x12\x12\n\x05up_id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x14\n\x07up_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07up_face\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08selected\x18\x04 \x01(\x03H\x03\x88\x01\x01\x42\x08\n\x06_up_idB\n\n\x08_up_nameB\n\n\x08_up_faceB\x0b\n\t_selectedb\x06proto3'
)




_UPARGS = _descriptor.Descriptor(
  name='UpArgs',
  full_name='com.bapis.bilibili.app.card.v1.UpArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='up_id', full_name='com.bapis.bilibili.app.card.v1.UpArgs.up_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='up_name', full_name='com.bapis.bilibili.app.card.v1.UpArgs.up_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='up_face', full_name='com.bapis.bilibili.app.card.v1.UpArgs.up_face', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='selected', full_name='com.bapis.bilibili.app.card.v1.UpArgs.selected', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
    _descriptor.OneofDescriptor(
      name='_up_id', full_name='com.bapis.bilibili.app.card.v1.UpArgs._up_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_up_name', full_name='com.bapis.bilibili.app.card.v1.UpArgs._up_name',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_up_face', full_name='com.bapis.bilibili.app.card.v1.UpArgs._up_face',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_selected', full_name='com.bapis.bilibili.app.card.v1.UpArgs._selected',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=88,
  serialized_end=230,
)

_UPARGS.oneofs_by_name['_up_id'].fields.append(
  _UPARGS.fields_by_name['up_id'])
_UPARGS.fields_by_name['up_id'].containing_oneof = _UPARGS.oneofs_by_name['_up_id']
_UPARGS.oneofs_by_name['_up_name'].fields.append(
  _UPARGS.fields_by_name['up_name'])
_UPARGS.fields_by_name['up_name'].containing_oneof = _UPARGS.oneofs_by_name['_up_name']
_UPARGS.oneofs_by_name['_up_face'].fields.append(
  _UPARGS.fields_by_name['up_face'])
_UPARGS.fields_by_name['up_face'].containing_oneof = _UPARGS.oneofs_by_name['_up_face']
_UPARGS.oneofs_by_name['_selected'].fields.append(
  _UPARGS.fields_by_name['selected'])
_UPARGS.fields_by_name['selected'].containing_oneof = _UPARGS.oneofs_by_name['_selected']
DESCRIPTOR.message_types_by_name['UpArgs'] = _UPARGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpArgs = _reflection.GeneratedProtocolMessageType('UpArgs', (_message.Message,), {
  'DESCRIPTOR' : _UPARGS,
  '__module__' : 'pyproto.com.bapis.bilibili.app.card.v1.UpArgs_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.card.v1.UpArgs)
  })
_sym_db.RegisterMessage(UpArgs)


# @@protoc_insertion_point(module_scope)
