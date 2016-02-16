# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from sqlalchemy.ext.declarative import declared_attr

from woodbox.db import db

from .node_model import NodeModel

class FolderNodeModel(NodeModel):
    id = db.Column(db.Integer, db.ForeignKey('node_model.id'), primary_key=True)

    title = db.Column(db.String(256), unique=False, nullable=True)

    content = db.relationship(NodeModel,
                              foreign_keys=NodeModel.parent_node_id,
                              back_populates='parent_node',
                              remote_side=NodeModel.parent_node_id)

    __mapper_args__ = {
        'polymorphic_identity': 'folder_node_model',
        'inherit_condition': (id == NodeModel.id),
    }
