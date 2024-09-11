# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/object_detector/proto/object_detector_options.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMmediapipe/tasks/cc/vision/object_detector/proto/object_detector_options.proto\x12,mediapipe.tasks.vision.object_detector.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xd5\x02\n\x15ObjectDetectorOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12 \n\x14\x64isplay_names_locale\x18\x02 \x01(\t:\x02\x65n\x12\x17\n\x0bmax_results\x18\x03 \x01(\x05:\x02-1\x12\x17\n\x0fscore_threshold\x18\x04 \x01(\x02\x12\x1a\n\x12\x63\x61tegory_allowlist\x18\x05 \x03(\t\x12\x19\n\x11\x63\x61tegory_denylist\x18\x06 \x03(\t2r\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8a\xc7\xb9\xd3\x01 \x01(\x0b\x32\x43.mediapipe.tasks.vision.object_detector.proto.ObjectDetectorOptionsBT\n6com.google.mediapipe.tasks.vision.objectdetector.protoB\x1aObjectDetectorOptionsProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.tasks.cc.vision.object_detector.proto.object_detector_options_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_OBJECTDETECTOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n6com.google.mediapipe.tasks.vision.objectdetector.protoB\032ObjectDetectorOptionsProto'
  _globals['_OBJECTDETECTOROPTIONS']._serialized_start=262
  _globals['_OBJECTDETECTOROPTIONS']._serialized_end=603
# @@protoc_insertion_point(module_scope)
