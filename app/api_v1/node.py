# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from marshmallow import post_dump
from marshmallow_jsonapi import fields

from woodbox.jsonapi_schema import JSONAPISchema, underscores_to_dashes, inflector

class NodeSchema(JSONAPISchema):
    node_type = fields.String(dump_only=True, attribute='type')

    owner = fields.Relationship(
        '/api/v1/users/{user_id}',
        related_url_kwargs={'user_id': '<owner.id>'},
        include_data=True,
        type_='users',
    )

    @post_dump
    def adapt_node_type(self, d):
        """Transform the node type to the JSON API type."""
        type_name = inflector.plural(d['node_type'][:-6])
        d['node_type'] = underscores_to_dashes(type_name)

    parent_node_id = fields.Integer(attribute='parent_node_id')
