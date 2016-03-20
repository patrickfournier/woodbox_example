# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from flask import g

from woodbox.db import db
from woodbox.push_service import NotificationService

from .user_model import UserModel

class NodeModel(db.Model):
    id = db.Column(db.Integer, db.Sequence('node_model_id_seq'), primary_key=True)
    type = db.Column(db.String(50))

    owner_id = db.Column(db.Integer, db.ForeignKey('user_model.id'), nullable=False)
    owner = db.relationship(UserModel, foreign_keys='NodeModel.owner_id')

    parent_node_id = db.Column(db.Integer, db.ForeignKey('folder_node_model.id'), nullable=True)
    parent_node = db.relationship('FolderNodeModel', foreign_keys='FolderNodeModel.parent_node_id')

    __mapper_args__ = {
        'polymorphic_identity': 'node_model',
        'polymorphic_on': type
    }

    def __init__(self, *args, **kwargs):
        # Force the owner to be the authenticated user.
        if 'user' in g:
            kwargs['owner_id'] = g.user
        super(NodeModel, self).__init__(*args, **kwargs)


NotificationService.register_model(NodeModel)
