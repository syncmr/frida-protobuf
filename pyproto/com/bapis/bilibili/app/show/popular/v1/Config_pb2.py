# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.show.popular.v1.Config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyproto.com.bapis.bilibili.app.show.popular.v1 import EntranceShow_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_EntranceShow__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.show.popular.v1.Config.proto',
  package='com.bapis.bilibili.app.show.popular.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;pyproto/com.bapis.bilibili.app.show.popular.v1.Config.proto\x12&com.bapis.bilibili.app.show.popular.v1\x1a\x41pyproto/com.bapis.bilibili.app.show.popular.v1.EntranceShow.proto\"\x97\x03\n\x06\x43onfig\x12\x17\n\nitem_title\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x62ottom_text\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11\x62ottom_text_cover\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1c\n\x0f\x62ottom_text_url\x18\x04 \x01(\tH\x03\x88\x01\x01\x12G\n\ttop_items\x18\x05 \x03(\x0b\x32\x34.com.bapis.bilibili.app.show.popular.v1.EntranceShow\x12\x17\n\nhead_image\x18\x06 \x01(\tH\x04\x88\x01\x01\x12H\n\npage_items\x18\x07 \x03(\x0b\x32\x34.com.bapis.bilibili.app.show.popular.v1.EntranceShow\x12\x10\n\x03hit\x18\x08 \x01(\x03H\x05\x88\x01\x01\x42\r\n\x0b_item_titleB\x0e\n\x0c_bottom_textB\x14\n\x12_bottom_text_coverB\x12\n\x10_bottom_text_urlB\r\n\x0b_head_imageB\x06\n\x04_hitb\x06proto3'
  ,
  dependencies=[pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_EntranceShow__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='com.bapis.bilibili.app.show.popular.v1.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_title', full_name='com.bapis.bilibili.app.show.popular.v1.Config.item_title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottom_text', full_name='com.bapis.bilibili.app.show.popular.v1.Config.bottom_text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottom_text_cover', full_name='com.bapis.bilibili.app.show.popular.v1.Config.bottom_text_cover', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottom_text_url', full_name='com.bapis.bilibili.app.show.popular.v1.Config.bottom_text_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top_items', full_name='com.bapis.bilibili.app.show.popular.v1.Config.top_items', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='head_image', full_name='com.bapis.bilibili.app.show.popular.v1.Config.head_image', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_items', full_name='com.bapis.bilibili.app.show.popular.v1.Config.page_items', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hit', full_name='com.bapis.bilibili.app.show.popular.v1.Config.hit', index=7,
      number=8, type=3, cpp_type=2, label=1,
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
      name='_item_title', full_name='com.bapis.bilibili.app.show.popular.v1.Config._item_title',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_bottom_text', full_name='com.bapis.bilibili.app.show.popular.v1.Config._bottom_text',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_bottom_text_cover', full_name='com.bapis.bilibili.app.show.popular.v1.Config._bottom_text_cover',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_bottom_text_url', full_name='com.bapis.bilibili.app.show.popular.v1.Config._bottom_text_url',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_head_image', full_name='com.bapis.bilibili.app.show.popular.v1.Config._head_image',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_hit', full_name='com.bapis.bilibili.app.show.popular.v1.Config._hit',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=171,
  serialized_end=578,
)

_CONFIG.fields_by_name['top_items'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_EntranceShow__pb2._ENTRANCESHOW
_CONFIG.fields_by_name['page_items'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_show_dot_popular_dot_v1_dot_EntranceShow__pb2._ENTRANCESHOW
_CONFIG.oneofs_by_name['_item_title'].fields.append(
  _CONFIG.fields_by_name['item_title'])
_CONFIG.fields_by_name['item_title'].containing_oneof = _CONFIG.oneofs_by_name['_item_title']
_CONFIG.oneofs_by_name['_bottom_text'].fields.append(
  _CONFIG.fields_by_name['bottom_text'])
_CONFIG.fields_by_name['bottom_text'].containing_oneof = _CONFIG.oneofs_by_name['_bottom_text']
_CONFIG.oneofs_by_name['_bottom_text_cover'].fields.append(
  _CONFIG.fields_by_name['bottom_text_cover'])
_CONFIG.fields_by_name['bottom_text_cover'].containing_oneof = _CONFIG.oneofs_by_name['_bottom_text_cover']
_CONFIG.oneofs_by_name['_bottom_text_url'].fields.append(
  _CONFIG.fields_by_name['bottom_text_url'])
_CONFIG.fields_by_name['bottom_text_url'].containing_oneof = _CONFIG.oneofs_by_name['_bottom_text_url']
_CONFIG.oneofs_by_name['_head_image'].fields.append(
  _CONFIG.fields_by_name['head_image'])
_CONFIG.fields_by_name['head_image'].containing_oneof = _CONFIG.oneofs_by_name['_head_image']
_CONFIG.oneofs_by_name['_hit'].fields.append(
  _CONFIG.fields_by_name['hit'])
_CONFIG.fields_by_name['hit'].containing_oneof = _CONFIG.oneofs_by_name['_hit']
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'pyproto.com.bapis.bilibili.app.show.popular.v1.Config_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.show.popular.v1.Config)
  })
_sym_db.RegisterMessage(Config)


# @@protoc_insertion_point(module_scope)
