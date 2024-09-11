# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/pose_detector/proto/pose_detector_graph_options.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOmediapipe/tasks/cc/vision/pose_detector/proto/pose_detector_graph_options.proto\x12*mediapipe.tasks.vision.pose_detector.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xb0\x02\n\x18PoseDetectorGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12%\n\x18min_detection_confidence\x18\x02 \x01(\x02:\x03\x30.5\x12&\n\x19min_suppression_threshold\x18\x03 \x01(\x02:\x03\x30.5\x12\x11\n\tnum_poses\x18\x04 \x01(\x05\x32s\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x9d\xae\xbb\xf5\x01 \x01(\x0b\x32\x44.mediapipe.tasks.vision.pose_detector.proto.PoseDetectorGraphOptionsBU\n4com.google.mediapipe.tasks.vision.posedetector.protoB\x1dPoseDetectorGraphOptionsProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.tasks.cc.vision.pose_detector.proto.pose_detector_graph_options_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_POSEDETECTORGRAPHOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n4com.google.mediapipe.tasks.vision.posedetector.protoB\035PoseDetectorGraphOptionsProto'
  _globals['_POSEDETECTORGRAPHOPTIONS']._serialized_start=262
  _globals['_POSEDETECTORGRAPHOPTIONS']._serialized_end=566
# @@protoc_insertion_point(module_scope)
