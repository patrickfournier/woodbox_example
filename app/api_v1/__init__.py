# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from flask import Blueprint, make_response, jsonify
from flask_restful import Api

from woodbox.access_control.api import Acl
from woodbox.access_control.record import Or, IsOwner, IsUser1, HasRole, InRecordACL
from woodbox.authenticator import HMACAuthenticator
from woodbox.models.user_model import WBRoleModel
from woodbox.record_api import make_api

from ..models.user_model import UserModel
from ..models.video_sequence_model import NodeModel, FolderNodeModel, DocumentNodeModel
from .user import UserSchema
from .video_sequence import NodeSchema, FolderNodeSchema, DocumentNodeSchema, ContentNodeSchema

blueprint = Blueprint('api_v1', __name__)
api = Api(blueprint)
api.authenticator = HMACAuthenticator()

@api.representation('application/vnd.api+json')
def output_jsonapi(data, code, headers=None):
    response = make_response(jsonify(data), code)
    response.headers.extend(headers or {})
    return response


api_acl = Acl()

# Grants
api_acl.grants({
    'admin': {
        'User': ['read'],
        'Node': ['create', 'read', 'update', 'delete'],
        'FolderNode': ['create', 'read', 'update', 'delete'],
        'DocumentNode': ['create', 'read', 'update', 'delete'],
        'ContentNode': ['read']
    },
    'user': {
        'User': ['read'],
        'Node': ['create', 'read', 'update', 'delete'],
        'FolderNode': ['create', 'read', 'update', 'delete'],
        'DocumentNode': ['create', 'read', 'update', 'delete'],
        'ContentNode': ['read']
    },
    WBRoleModel.anonymous_role_name: {
        'User': ['read'],
        'Node': ['read'],
        'ContentNode': ['read']
    }
})

make_api(api, 'User', UserModel, UserSchema,
         api_authorizers=[api_acl.authorize])

make_api(api, 'Node', NodeModel, NodeSchema,
         api_authorizers=[api_acl.authorize],
         record_authorizer=IsOwner())

make_api(api, 'FolderNode', FolderNodeModel, FolderNodeSchema,
         api_authorizers=[api_acl.authorize])

make_api(api, 'DocumentNode', DocumentNodeModel, DocumentNodeSchema,
         api_authorizers=[api_acl.authorize])

make_api(api, 'ContentNode', NodeModel, ContentNodeSchema,
         api_authorizers=[api_acl.authorize],
         record_authorizer=Or(IsOwner(), InRecordACL(), IsUser1(), HasRole(['admin'])))
