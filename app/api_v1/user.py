# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from marshmallow_jsonapi import fields

from woodbox.jsonapi_schema import JSONAPISchema

class RoleSchema(JSONAPISchema):
    rolename = fields.String(attribute='rolename')

class UserSchema(JSONAPISchema):
    """A schema for models.user_model.HumanModel."""
    username = fields.String(attribute='username')
    name = fields.String(attribute='name')
    roles = fields.Nested('RoleSchema', many=True)
