# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from marshmallow_jsonapi import fields

from woodbox.jsonapi_schema import JSONAPISchema, underscores_to_dashes

from ..models.document_node_model import DocumentNodeModel
from ..models.folder_node_model import FolderNodeModel

class ContentNodeSchema(JSONAPISchema):
    title = fields.Method('get_title')
    node_type = fields.Method('get_type')

    owner = fields.Relationship(
        '/api/v1/users/{user_id}',  # FIXME: find a way to get this
                                    # URL; the code is executed before
                                    # the blueprint is registered.
        related_url_kwargs={'user_id': '<owner.id>'},
        include_data=True,
        type_='users',
    )

    def get_title(self, obj):
        if isinstance(obj, FolderNodeModel):
            return obj.title
        elif isinstance(obj, DocumentNodeModel):
            return obj.document.title
        return ''

    def get_type(self, obj):
        type_name = obj.type[:-6]
        return underscores_to_dashes(type_name)
