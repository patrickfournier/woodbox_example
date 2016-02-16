# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from marshmallow_jsonapi import fields

from .node import NodeSchema

class FolderNodeSchema(NodeSchema):
    parent_folder = fields.Nested('self', many=False, attribute='parent_node', exclude=('content',))
    title = fields.String()
    content = fields.Nested(NodeSchema, many=True, exclude=('parent_node',))
