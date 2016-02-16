# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from woodbox.db import db

class DocumentModel(db.Model):
    id = db.Column(db.Integer, db.Sequence('document_model_id_seq'), primary_key=True)
    document_type = db.Column(db.String(50))

    title = db.Column(db.String(256), unique=False, nullable=False)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    __mapper_args__ = {
        'polymorphic_identity': 'document_model',
        'polymorphic_on': document_type
    }
