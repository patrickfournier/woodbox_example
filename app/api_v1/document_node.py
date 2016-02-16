# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from marshmallow_jsonapi import fields

from .node import NodeSchema
from .document import DocumentSchema

class DocumentNodeSchema(NodeSchema):
    parent_folder = fields.Nested('self', many=False, attribute='parent_node', exclude=('content',))
    document = fields.Nested(DocumentSchema, many=False)
