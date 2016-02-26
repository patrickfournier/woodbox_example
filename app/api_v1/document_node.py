# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from marshmallow_jsonapi import fields

from .node import NodeSchema
from .document import DocumentSchema

class DocumentNodeSchema(NodeSchema):
    document = fields.Relationship(
        '/api/v1/documents/{document_id}',  # FIXME: find a way to get
                                            # this URL; the code is
                                            # executed before the
                                            # blueprint is registered.
        related_url_kwargs={'document_id': '<document.id>'},
        include_data=True,
        type_='documents',
    )
