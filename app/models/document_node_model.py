# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from woodbox.db import db

from .document_model import DocumentModel
from .node_model import NodeModel

class DocumentNodeModel(NodeModel):
    id = db.Column(db.Integer, db.ForeignKey('node_model.id'), primary_key=True)

    document_id = db.Column(db.Integer, db.ForeignKey('document_model.id'), nullable=False)
    document = db.relationship(DocumentModel,
                               foreign_keys='DocumentNodeModel.document_id', single_parent=True,
                               cascade='all, delete-orphan')

    __mapper_args__ = {
        'polymorphic_identity': 'document_node_model',
    }
