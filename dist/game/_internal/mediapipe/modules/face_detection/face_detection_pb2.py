# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/modules/face_detection/face_detection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.calculators.tensor import inference_calculator_pb2 as mediapipe_dot_calculators_dot_tensor_dot_inference__calculator__pb2
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.gpu import gpu_origin_pb2 as mediapipe_dot_gpu_dot_gpu__origin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5mediapipe/modules/face_detection/face_detection.proto\x12\tmediapipe\x1a\x37mediapipe/calculators/tensor/inference_calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x1emediapipe/gpu/gpu_origin.proto\"\xe6\x03\n\x14\x46\x61\x63\x65\x44\x65tectionOptions\x12\x12\n\nmodel_path\x18\x01 \x01(\t\x12-\n\ngpu_origin\x18\x0b \x01(\x0e\x32\x19.mediapipe.GpuOrigin.Mode\x12\x14\n\x0ctensor_width\x18\x15 \x01(\x05\x12\x15\n\rtensor_height\x18\x16 \x01(\x05\x12\x12\n\nnum_layers\x18\x17 \x01(\x05\x12\x0f\n\x07strides\x18\x18 \x03(\x05\x12*\n\x1finterpolated_scale_aspect_ratio\x18\x19 \x01(\x02:\x01\x31\x12\x11\n\tnum_boxes\x18\x1f \x01(\x05\x12\x12\n\x07x_scale\x18  \x01(\x02:\x01\x30\x12\x12\n\x07y_scale\x18! \x01(\x02:\x01\x30\x12\x12\n\x07w_scale\x18\" \x01(\x02:\x01\x30\x12\x12\n\x07h_scale\x18# \x01(\x02:\x01\x30\x12\x18\n\x10min_score_thresh\x18$ \x01(\x02\x12@\n\x08\x64\x65legate\x18\x06 \x01(\x0b\x32..mediapipe.InferenceCalculatorOptions.Delegate2N\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xee\xf3\xbc\xb2\x01 \x01(\x0b\x32\x1f.mediapipe.FaceDetectionOptionsBE\n*com.google.mediapipe.modules.facedetectionB\x17\x46\x61\x63\x65\x44\x65tectionFrontProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.modules.face_detection.face_detection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_FACEDETECTIONOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n*com.google.mediapipe.modules.facedetectionB\027FaceDetectionFrontProto'
  _globals['_FACEDETECTIONOPTIONS']._serialized_start=204
  _globals['_FACEDETECTIONOPTIONS']._serialized_end=690
# @@protoc_insertion_point(module_scope)
