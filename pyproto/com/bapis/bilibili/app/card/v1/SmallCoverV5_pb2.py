# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.card.v1.SmallCoverV5.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyproto.com.bapis.bilibili.app.card.v1 import ReasonStyle_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import Up_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Up__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import Base_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import HotwordEntrance_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_HotwordEntrance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.card.v1.SmallCoverV5.proto',
  package='com.bapis.bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9pyproto/com.bapis.bilibili.app.card.v1.SmallCoverV5.proto\x12\x1e\x63om.bapis.bilibili.app.card.v1\x1a\x38pyproto/com.bapis.bilibili.app.card.v1.ReasonStyle.proto\x1a/pyproto/com.bapis.bilibili.app.card.v1.Up.proto\x1a\x31pyproto/com.bapis.bilibili.app.card.v1.Base.proto\x1a<pyproto/com.bapis.bilibili.app.card.v1.HotwordEntrance.proto\"\xe2\x07\n\x0cSmallCoverV5\x12\x37\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32$.com.bapis.bilibili.app.card.v1.BaseH\x00\x88\x01\x01\x12\x16\n\tcover_gif\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x33\n\x02up\x18\x03 \x01(\x0b\x32\".com.bapis.bilibili.app.card.v1.UpH\x02\x88\x01\x01\x12\x1f\n\x12\x63over_right_text_1\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x19\n\x0cright_desc_1\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x19\n\x0cright_desc_2\x18\x06 \x01(\tH\x05\x88\x01\x01\x12K\n\x11rcmd_reason_style\x18\x07 \x01(\x0b\x32+.com.bapis.bilibili.app.card.v1.ReasonStyleH\x06\x88\x01\x01\x12N\n\x10hotword_entrance\x18\x08 \x01(\x0b\x32/.com.bapis.bilibili.app.card.v1.HotwordEntranceH\x07\x88\x01\x01\x12K\n\x11\x63orner_mark_style\x18\t \x01(\x0b\x32+.com.bapis.bilibili.app.card.v1.ReasonStyleH\x08\x88\x01\x01\x12\x19\n\x0cright_icon_1\x18\n \x01(\x05H\t\x88\x01\x01\x12\x19\n\x0cright_icon_2\x18\x0b \x01(\x05H\n\x88\x01\x01\x12P\n\x16left_corner_mark_style\x18\x0c \x01(\x0b\x32+.com.bapis.bilibili.app.card.v1.ReasonStyleH\x0b\x88\x01\x01\x12\x31\n$cover_right_text_content_description\x18\r \x01(\tH\x0c\x88\x01\x01\x12-\n right_desc_1_content_description\x18\x0e \x01(\tH\r\x88\x01\x01\x42\x07\n\x05_baseB\x0c\n\n_cover_gifB\x05\n\x03_upB\x15\n\x13_cover_right_text_1B\x0f\n\r_right_desc_1B\x0f\n\r_right_desc_2B\x14\n\x12_rcmd_reason_styleB\x13\n\x11_hotword_entranceB\x14\n\x12_corner_mark_styleB\x0f\n\r_right_icon_1B\x0f\n\r_right_icon_2B\x19\n\x17_left_corner_mark_styleB\'\n%_cover_right_text_content_descriptionB#\n!_right_desc_1_content_descriptionb\x06proto3'
  ,
  dependencies=[pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Up__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_HotwordEntrance__pb2.DESCRIPTOR,])




_SMALLCOVERV5 = _descriptor.Descriptor(
  name='SmallCoverV5',
  full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.base', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cover_gif', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.cover_gif', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='up', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.up', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cover_right_text_1', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.cover_right_text_1', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right_desc_1', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.right_desc_1', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right_desc_2', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.right_desc_2', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rcmd_reason_style', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.rcmd_reason_style', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hotword_entrance', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.hotword_entrance', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='corner_mark_style', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.corner_mark_style', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right_icon_1', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.right_icon_1', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right_icon_2', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.right_icon_2', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left_corner_mark_style', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.left_corner_mark_style', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cover_right_text_content_description', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.cover_right_text_content_description', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right_desc_1_content_description', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5.right_desc_1_content_description', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_base', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._base',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_cover_gif', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._cover_gif',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_up', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._up',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_cover_right_text_1', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._cover_right_text_1',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_right_desc_1', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._right_desc_1',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_right_desc_2', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._right_desc_2',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_rcmd_reason_style', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._rcmd_reason_style',
      index=6, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_hotword_entrance', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._hotword_entrance',
      index=7, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_corner_mark_style', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._corner_mark_style',
      index=8, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_right_icon_1', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._right_icon_1',
      index=9, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_right_icon_2', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._right_icon_2',
      index=10, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_left_corner_mark_style', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._left_corner_mark_style',
      index=11, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_cover_right_text_content_description', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._cover_right_text_content_description',
      index=12, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_right_desc_1_content_description', full_name='com.bapis.bilibili.app.card.v1.SmallCoverV5._right_desc_1_content_description',
      index=13, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=314,
  serialized_end=1308,
)

_SMALLCOVERV5.fields_by_name['base'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Base__pb2._BASE
_SMALLCOVERV5.fields_by_name['up'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Up__pb2._UP
_SMALLCOVERV5.fields_by_name['rcmd_reason_style'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2._REASONSTYLE
_SMALLCOVERV5.fields_by_name['hotword_entrance'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_HotwordEntrance__pb2._HOTWORDENTRANCE
_SMALLCOVERV5.fields_by_name['corner_mark_style'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2._REASONSTYLE
_SMALLCOVERV5.fields_by_name['left_corner_mark_style'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_ReasonStyle__pb2._REASONSTYLE
_SMALLCOVERV5.oneofs_by_name['_base'].fields.append(
  _SMALLCOVERV5.fields_by_name['base'])
_SMALLCOVERV5.fields_by_name['base'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_base']
_SMALLCOVERV5.oneofs_by_name['_cover_gif'].fields.append(
  _SMALLCOVERV5.fields_by_name['cover_gif'])
_SMALLCOVERV5.fields_by_name['cover_gif'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_cover_gif']
_SMALLCOVERV5.oneofs_by_name['_up'].fields.append(
  _SMALLCOVERV5.fields_by_name['up'])
_SMALLCOVERV5.fields_by_name['up'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_up']
_SMALLCOVERV5.oneofs_by_name['_cover_right_text_1'].fields.append(
  _SMALLCOVERV5.fields_by_name['cover_right_text_1'])
_SMALLCOVERV5.fields_by_name['cover_right_text_1'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_cover_right_text_1']
_SMALLCOVERV5.oneofs_by_name['_right_desc_1'].fields.append(
  _SMALLCOVERV5.fields_by_name['right_desc_1'])
_SMALLCOVERV5.fields_by_name['right_desc_1'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_right_desc_1']
_SMALLCOVERV5.oneofs_by_name['_right_desc_2'].fields.append(
  _SMALLCOVERV5.fields_by_name['right_desc_2'])
_SMALLCOVERV5.fields_by_name['right_desc_2'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_right_desc_2']
_SMALLCOVERV5.oneofs_by_name['_rcmd_reason_style'].fields.append(
  _SMALLCOVERV5.fields_by_name['rcmd_reason_style'])
_SMALLCOVERV5.fields_by_name['rcmd_reason_style'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_rcmd_reason_style']
_SMALLCOVERV5.oneofs_by_name['_hotword_entrance'].fields.append(
  _SMALLCOVERV5.fields_by_name['hotword_entrance'])
_SMALLCOVERV5.fields_by_name['hotword_entrance'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_hotword_entrance']
_SMALLCOVERV5.oneofs_by_name['_corner_mark_style'].fields.append(
  _SMALLCOVERV5.fields_by_name['corner_mark_style'])
_SMALLCOVERV5.fields_by_name['corner_mark_style'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_corner_mark_style']
_SMALLCOVERV5.oneofs_by_name['_right_icon_1'].fields.append(
  _SMALLCOVERV5.fields_by_name['right_icon_1'])
_SMALLCOVERV5.fields_by_name['right_icon_1'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_right_icon_1']
_SMALLCOVERV5.oneofs_by_name['_right_icon_2'].fields.append(
  _SMALLCOVERV5.fields_by_name['right_icon_2'])
_SMALLCOVERV5.fields_by_name['right_icon_2'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_right_icon_2']
_SMALLCOVERV5.oneofs_by_name['_left_corner_mark_style'].fields.append(
  _SMALLCOVERV5.fields_by_name['left_corner_mark_style'])
_SMALLCOVERV5.fields_by_name['left_corner_mark_style'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_left_corner_mark_style']
_SMALLCOVERV5.oneofs_by_name['_cover_right_text_content_description'].fields.append(
  _SMALLCOVERV5.fields_by_name['cover_right_text_content_description'])
_SMALLCOVERV5.fields_by_name['cover_right_text_content_description'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_cover_right_text_content_description']
_SMALLCOVERV5.oneofs_by_name['_right_desc_1_content_description'].fields.append(
  _SMALLCOVERV5.fields_by_name['right_desc_1_content_description'])
_SMALLCOVERV5.fields_by_name['right_desc_1_content_description'].containing_oneof = _SMALLCOVERV5.oneofs_by_name['_right_desc_1_content_description']
DESCRIPTOR.message_types_by_name['SmallCoverV5'] = _SMALLCOVERV5
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SmallCoverV5 = _reflection.GeneratedProtocolMessageType('SmallCoverV5', (_message.Message,), {
  'DESCRIPTOR' : _SMALLCOVERV5,
  '__module__' : 'pyproto.com.bapis.bilibili.app.card.v1.SmallCoverV5_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.card.v1.SmallCoverV5)
  })
_sym_db.RegisterMessage(SmallCoverV5)


# @@protoc_insertion_point(module_scope)
