# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crx3.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncrx3.proto\x12\x08\x63rx_file\"\xb7\x01\n\rCrxFileHeader\x12\x35\n\x0fsha256_with_rsa\x18\x02 \x03(\x0b\x32\x1c.crx_file.AsymmetricKeyProof\x12\x37\n\x11sha256_with_ecdsa\x18\x03 \x03(\x0b\x32\x1c.crx_file.AsymmetricKeyProof\x12\x19\n\x11verified_contents\x18\x04 \x01(\x0c\x12\x1b\n\x12signed_header_data\x18\x90N \x01(\x0c\";\n\x12\x41symmetricKeyProof\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\x1c\n\nSignedData\x12\x0e\n\x06\x63rx_id\x18\x01 \x01(\x0c\x42\x02H\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crx3_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003'
  _globals['_CRXFILEHEADER']._serialized_start=25
  _globals['_CRXFILEHEADER']._serialized_end=208
  _globals['_ASYMMETRICKEYPROOF']._serialized_start=210
  _globals['_ASYMMETRICKEYPROOF']._serialized_end=269
  _globals['_SIGNEDDATA']._serialized_start=271
  _globals['_SIGNEDDATA']._serialized_end=299
# @@protoc_insertion_point(module_scope)
