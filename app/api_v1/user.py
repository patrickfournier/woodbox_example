# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from marshmallow import pre_load, post_dump
from marshmallow_jsonapi import fields

from woodbox.jsonapi_schema import JSONAPISchema, underscores_to_dashes, inflector

class RoleSchema(JSONAPISchema):
    rolename = fields.String(attribute='rolename')

class UserSchema(JSONAPISchema):
    """A schema for models.user_model.HumanModel."""
    username = fields.String(attribute='username')
    name = fields.String(attribute='name')
    roles = fields.Nested('RoleSchema', many=True)
