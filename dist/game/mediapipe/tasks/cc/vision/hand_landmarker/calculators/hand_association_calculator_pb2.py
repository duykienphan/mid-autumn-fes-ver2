# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/hand_landmarker/calculators/hand_association_calculator.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nWmediapipe/tasks/cc/vision/hand_landmarker/calculators/hand_association_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xa3\x01\n HandAssociationCalculatorOptions\x12#\n\x18min_similarity_threshold\x18\x01 \x01(\x02:\x01\x31\x32Z\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8f\xa1\xd5\xc2\x01 \x01(\x0b\x32+.mediapipe.HandAssociationCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.tasks.cc.vision.hand_landmarker.calculators.hand_association_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_HANDASSOCIATIONCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _globals['_HANDASSOCIATIONCALCULATOROPTIONS']._serialized_start=141
  _globals['_HANDASSOCIATIONCALCULATOROPTIONS']._serialized_end=304
# @@protoc_insertion_point(module_scope)
