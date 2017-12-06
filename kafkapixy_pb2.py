# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kafkapixy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kafkapixy.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0fkafkapixy.proto\"w\n\x06ProdRq\x12\x0f\n\x07\x63luster\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x11\n\tkey_value\x18\x03 \x01(\x0c\x12\x15\n\rkey_undefined\x18\x04 \x01(\x08\x12\x0f\n\x07message\x18\x05 \x01(\x0c\x12\x12\n\nasync_mode\x18\x06 \x01(\x08\"+\n\x06ProdRs\x12\x11\n\tpartition\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x03\"\x88\x01\n\nConsNAckRq\x12\x0f\n\x07\x63luster\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\r\n\x05group\x18\x03 \x01(\t\x12\x0e\n\x06no_ack\x18\x04 \x01(\x08\x12\x10\n\x08\x61uto_ack\x18\x05 \x01(\x08\x12\x15\n\rack_partition\x18\x06 \x01(\x05\x12\x12\n\nack_offset\x18\x07 \x01(\x03\"f\n\x06\x43onsRs\x12\x11\n\tpartition\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x11\n\tkey_value\x18\x03 \x01(\x0c\x12\x15\n\rkey_undefined\x18\x04 \x01(\x08\x12\x0f\n\x07message\x18\x05 \x01(\x0c\"Y\n\x05\x41\x63kRq\x12\x0f\n\x07\x63luster\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\r\n\x05group\x18\x03 \x01(\t\x12\x11\n\tpartition\x18\x04 \x01(\x05\x12\x0e\n\x06offset\x18\x05 \x01(\x03\"\x07\n\x05\x41\x63kRs\"\x93\x01\n\x0fPartitionOffset\x12\x11\n\tpartition\x18\x01 \x01(\x05\x12\r\n\x05\x62\x65gin\x18\x02 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x03\x12\r\n\x05\x63ount\x18\x04 \x01(\x03\x12\x0e\n\x06offset\x18\x05 \x01(\x03\x12\x0b\n\x03lag\x18\x06 \x01(\x03\x12\x10\n\x08metadata\x18\x07 \x01(\t\x12\x13\n\x0bsparse_acks\x18\x08 \x01(\t\"=\n\x0cGetOffsetsRq\x12\x0f\n\x07\x63luster\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\r\n\x05group\x18\x03 \x01(\t\"1\n\x0cGetOffsetsRs\x12!\n\x07offsets\x18\x01 \x03(\x0b\x32\x10.PartitionOffset2\x98\x01\n\tKafkaPixy\x12\x1d\n\x07Produce\x12\x07.ProdRq\x1a\x07.ProdRs\"\x00\x12%\n\x0b\x43onsumeNAck\x12\x0b.ConsNAckRq\x1a\x07.ConsRs\"\x00\x12\x17\n\x03\x41\x63k\x12\x06.AckRq\x1a\x06.AckRs\"\x00\x12,\n\nGetOffsets\x12\r.GetOffsetsRq\x1a\r.GetOffsetsRs\"\x00\x42\x04Z\x02pbb\x06proto3')
)




_PRODRQ = _descriptor.Descriptor(
  name='ProdRq',
  full_name='ProdRq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='ProdRq.cluster', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topic', full_name='ProdRq.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_value', full_name='ProdRq.key_value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_undefined', full_name='ProdRq.key_undefined', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='ProdRq.message', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='async_mode', full_name='ProdRq.async_mode', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=138,
)


_PRODRS = _descriptor.Descriptor(
  name='ProdRs',
  full_name='ProdRs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partition', full_name='ProdRs.partition', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='ProdRs.offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=183,
)


_CONSNACKRQ = _descriptor.Descriptor(
  name='ConsNAckRq',
  full_name='ConsNAckRq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='ConsNAckRq.cluster', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topic', full_name='ConsNAckRq.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='ConsNAckRq.group', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='no_ack', full_name='ConsNAckRq.no_ack', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auto_ack', full_name='ConsNAckRq.auto_ack', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ack_partition', full_name='ConsNAckRq.ack_partition', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ack_offset', full_name='ConsNAckRq.ack_offset', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=322,
)


_CONSRS = _descriptor.Descriptor(
  name='ConsRs',
  full_name='ConsRs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partition', full_name='ConsRs.partition', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='ConsRs.offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_value', full_name='ConsRs.key_value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_undefined', full_name='ConsRs.key_undefined', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='ConsRs.message', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=426,
)


_ACKRQ = _descriptor.Descriptor(
  name='AckRq',
  full_name='AckRq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='AckRq.cluster', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topic', full_name='AckRq.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='AckRq.group', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partition', full_name='AckRq.partition', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='AckRq.offset', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=517,
)


_ACKRS = _descriptor.Descriptor(
  name='AckRs',
  full_name='AckRs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=526,
)


_PARTITIONOFFSET = _descriptor.Descriptor(
  name='PartitionOffset',
  full_name='PartitionOffset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partition', full_name='PartitionOffset.partition', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='begin', full_name='PartitionOffset.begin', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='PartitionOffset.end', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='PartitionOffset.count', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='PartitionOffset.offset', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lag', full_name='PartitionOffset.lag', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='PartitionOffset.metadata', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sparse_acks', full_name='PartitionOffset.sparse_acks', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=676,
)


_GETOFFSETSRQ = _descriptor.Descriptor(
  name='GetOffsetsRq',
  full_name='GetOffsetsRq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='GetOffsetsRq.cluster', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topic', full_name='GetOffsetsRq.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='GetOffsetsRq.group', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=678,
  serialized_end=739,
)


_GETOFFSETSRS = _descriptor.Descriptor(
  name='GetOffsetsRs',
  full_name='GetOffsetsRs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offsets', full_name='GetOffsetsRs.offsets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=790,
)

_GETOFFSETSRS.fields_by_name['offsets'].message_type = _PARTITIONOFFSET
DESCRIPTOR.message_types_by_name['ProdRq'] = _PRODRQ
DESCRIPTOR.message_types_by_name['ProdRs'] = _PRODRS
DESCRIPTOR.message_types_by_name['ConsNAckRq'] = _CONSNACKRQ
DESCRIPTOR.message_types_by_name['ConsRs'] = _CONSRS
DESCRIPTOR.message_types_by_name['AckRq'] = _ACKRQ
DESCRIPTOR.message_types_by_name['AckRs'] = _ACKRS
DESCRIPTOR.message_types_by_name['PartitionOffset'] = _PARTITIONOFFSET
DESCRIPTOR.message_types_by_name['GetOffsetsRq'] = _GETOFFSETSRQ
DESCRIPTOR.message_types_by_name['GetOffsetsRs'] = _GETOFFSETSRS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProdRq = _reflection.GeneratedProtocolMessageType('ProdRq', (_message.Message,), dict(
  DESCRIPTOR = _PRODRQ,
  __module__ = 'kafkapixy_pb2'
  # @@protoc_insertion_point(class_scope:ProdRq)
  ))
_sym_db.RegisterMessage(ProdRq)

ProdRs = _reflection.GeneratedProtocolMessageType('ProdRs', (_message.Message,), dict(
  DESCRIPTOR = _PRODRS,
  __module__ = 'kafkapixy_pb2'
  # @@protoc_insertion_point(class_scope:ProdRs)
  ))
_sym_db.RegisterMessage(ProdRs)

ConsNAckRq = _reflection.GeneratedProtocolMessageType('ConsNAckRq', (_message.Message,), dict(
  DESCRIPTOR = _CONSNACKRQ,
  __module__ = 'kafkapixy_pb2'
  # @@protoc_insertion_point(class_scope:ConsNAckRq)
  ))
_sym_db.RegisterMessage(ConsNAckRq)

ConsRs = _reflection.GeneratedProtocolMessageType('ConsRs', (_message.Message,), dict(
  DESCRIPTOR = _CONSRS,
  __module__ = 'kafkapixy_pb2'
  # @@protoc_insertion_point(class_scope:ConsRs)
  ))
_sym_db.RegisterMessage(ConsRs)

AckRq = _reflection.GeneratedProtocolMessageType('AckRq', (_message.Message,), dict(
  DESCRIPTOR = _ACKRQ,
  __module__ = 'kafkapixy_pb2'
  # @@protoc_insertion_point(class_scope:AckRq)
  ))
_sym_db.RegisterMessage(AckRq)

AckRs = _reflection.GeneratedProtocolMessageType('AckRs', (_message.Message,), dict(
  DESCRIPTOR = _ACKRS,
  __module__ = 'kafkapixy_pb2'
  # @@protoc_insertion_point(class_scope:AckRs)
  ))
_sym_db.RegisterMessage(AckRs)

PartitionOffset = _reflection.GeneratedProtocolMessageType('PartitionOffset', (_message.Message,), dict(
  DESCRIPTOR = _PARTITIONOFFSET,
  __module__ = 'kafkapixy_pb2'
  # @@protoc_insertion_point(class_scope:PartitionOffset)
  ))
_sym_db.RegisterMessage(PartitionOffset)

GetOffsetsRq = _reflection.GeneratedProtocolMessageType('GetOffsetsRq', (_message.Message,), dict(
  DESCRIPTOR = _GETOFFSETSRQ,
  __module__ = 'kafkapixy_pb2'
  # @@protoc_insertion_point(class_scope:GetOffsetsRq)
  ))
_sym_db.RegisterMessage(GetOffsetsRq)

GetOffsetsRs = _reflection.GeneratedProtocolMessageType('GetOffsetsRs', (_message.Message,), dict(
  DESCRIPTOR = _GETOFFSETSRS,
  __module__ = 'kafkapixy_pb2'
  # @@protoc_insertion_point(class_scope:GetOffsetsRs)
  ))
_sym_db.RegisterMessage(GetOffsetsRs)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\002pb'))

_KAFKAPIXY = _descriptor.ServiceDescriptor(
  name='KafkaPixy',
  full_name='KafkaPixy',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=793,
  serialized_end=945,
  methods=[
  _descriptor.MethodDescriptor(
    name='Produce',
    full_name='KafkaPixy.Produce',
    index=0,
    containing_service=None,
    input_type=_PRODRQ,
    output_type=_PRODRS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ConsumeNAck',
    full_name='KafkaPixy.ConsumeNAck',
    index=1,
    containing_service=None,
    input_type=_CONSNACKRQ,
    output_type=_CONSRS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Ack',
    full_name='KafkaPixy.Ack',
    index=2,
    containing_service=None,
    input_type=_ACKRQ,
    output_type=_ACKRS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetOffsets',
    full_name='KafkaPixy.GetOffsets',
    index=3,
    containing_service=None,
    input_type=_GETOFFSETSRQ,
    output_type=_GETOFFSETSRS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_KAFKAPIXY)

DESCRIPTOR.services_by_name['KafkaPixy'] = _KAFKAPIXY

# @@protoc_insertion_point(module_scope)
