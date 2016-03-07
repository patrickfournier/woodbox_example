# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from datetime import datetime

from marshmallow_jsonapi import fields

from woodbox.jsonapi_schema import JSONAPISchema

class DocumentSchema(JSONAPISchema):
    document_type = fields.String()
    title = fields.String()
    body = fields.String()
    date_created = fields.DateTime(allow_none=True, missing=datetime.utcnow())
    date_modified = fields.DateTime(allow_none=True, missing=datetime.utcnow())
