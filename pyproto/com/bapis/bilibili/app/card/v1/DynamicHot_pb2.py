# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.card.v1.DynamicHot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyproto.com.bapis.bilibili.app.card.v1 import ReasonStyle_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import Base_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.card.v1.DynamicHot.proto',
  package='com.bapis.bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7pyproto/com.bapis.bilibili.app.card.v1.DynamicHot.proto\x12\x1e\x63om.bapis.bilibili.app.card.v1\x1a\x38pyproto/com.bapis.bilibili.app.card.v1.ReasonStyle.proto\x1a\x31pyproto/com.bapis.bilibili.app.card.v1.Base.proto\"\xf7\x02\n\nDynamicHot\x12\x37\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32$.com.bapis.bilibili.app.card.v1.BaseH\x00\x88\x01\x01\x12\x1b\n\x0etop_left_title\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08more_uri\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tmore_text\x18\x06 \x01(\tH\x03\x88\x01\x01\x12\x0e\n\x06\x63overs\x18\x07 \x03(\t\x12\x1d\n\x10\x63over_right_text\x18\x08 \x01(\tH\x04\x88\x01\x01\x12O\n\x15top_rcmd_reason_style\x18\t \x01(\x0b\x32+.com.bapis.bilibili.app.card.v1.ReasonStyleH\x05\x88\x01\x01\x42\x07\n\x05_baseB\x11\n\x0f_top_left_titleB\x0b\n\t_more_uriB\x0c\n\n_more_textB\x13\n\x11_cover_right_textB\x18\n\x16_top_rcmd_reason_styleb\x06proto3'
  ,
  dependencies=[pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2.DESCRIPTOR,])




_DYNAMICHOT = _descriptor.Descriptor(
  name='DynamicHot',
  full_name='com.bapis.bilibili.app.card.v1.DynamicHot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='com.bapis.bilibili.app.card.v1.DynamicHot.base', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top_left_title', full_name='com.bapis.bilibili.app.card.v1.DynamicHot.top_left_title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='more_uri', full_name='com.bapis.bilibili.app.card.v1.DynamicHot.more_uri', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='more_text', full_name='com.bapis.bilibili.app.card.v1.DynamicHot.more_text', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='covers', full_name='com.bapis.bilibili.app.card.v1.DynamicHot.covers', index=4,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cover_right_text', full_name='com.bapis.bilibili.app.card.v1.DynamicHot.cover_right_text', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top_rcmd_reason_style', full_name='com.bapis.bilibili.app.card.v1.DynamicHot.top_rcmd_reason_style', index=6,
      number=9, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='_base', full_name='com.bapis.bilibili.app.card.v1.DynamicHot._base',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_top_left_title', full_name='com.bapis.bilibili.app.card.v1.DynamicHot._top_left_title',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_more_uri', full_name='com.bapis.bilibili.app.card.v1.DynamicHot._more_uri',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_more_text', full_name='com.bapis.bilibili.app.card.v1.DynamicHot._more_text',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_cover_right_text', full_name='com.bapis.bilibili.app.card.v1.DynamicHot._cover_right_text',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_top_rcmd_reason_style', full_name='com.bapis.bilibili.app.card.v1.DynamicHot._top_rcmd_reason_style',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=201,
  serialized_end=576,
)

_DYNAMICHOT.fields_by_name['base'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2._BASE
_DYNAMICHOT.fields_by_name['top_rcmd_reason_style'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2._REASONSTYLE
_DYNAMICHOT.oneofs_by_name['_base'].fields.append(
  _DYNAMICHOT.fields_by_name['base'])
_DYNAMICHOT.fields_by_name['base'].containing_oneof = _DYNAMICHOT.oneofs_by_name['_base']
_DYNAMICHOT.oneofs_by_name['_top_left_title'].fields.append(
  _DYNAMICHOT.fields_by_name['top_left_title'])
_DYNAMICHOT.fields_by_name['top_left_title'].containing_oneof = _DYNAMICHOT.oneofs_by_name['_top_left_title']
_DYNAMICHOT.oneofs_by_name['_more_uri'].fields.append(
  _DYNAMICHOT.fields_by_name['more_uri'])
_DYNAMICHOT.fields_by_name['more_uri'].containing_oneof = _DYNAMICHOT.oneofs_by_name['_more_uri']
_DYNAMICHOT.oneofs_by_name['_more_text'].fields.append(
  _DYNAMICHOT.fields_by_name['more_text'])
_DYNAMICHOT.fields_by_name['more_text'].containing_oneof = _DYNAMICHOT.oneofs_by_name['_more_text']
_DYNAMICHOT.oneofs_by_name['_cover_right_text'].fields.append(
  _DYNAMICHOT.fields_by_name['cover_right_text'])
_DYNAMICHOT.fields_by_name['cover_right_text'].containing_oneof = _DYNAMICHOT.oneofs_by_name['_cover_right_text']
_DYNAMICHOT.oneofs_by_name['_top_rcmd_reason_style'].fields.append(
  _DYNAMICHOT.fields_by_name['top_rcmd_reason_style'])
_DYNAMICHOT.fields_by_name['top_rcmd_reason_style'].containing_oneof = _DYNAMICHOT.oneofs_by_name['_top_rcmd_reason_style']
DESCRIPTOR.message_types_by_name['DynamicHot'] = _DYNAMICHOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DynamicHot = _reflection.GeneratedProtocolMessageType('DynamicHot', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMICHOT,
  '__module__' : 'pyproto.com.bapis.bilibili.app.card.v1.DynamicHot_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.card.v1.DynamicHot)
  })
_sym_db.RegisterMessage(DynamicHot)


# @@protoc_insertion_point(module_scope)
