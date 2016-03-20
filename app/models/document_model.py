# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import arrow

from sqlalchemy_utils import ArrowType

from woodbox.db import db

class DocumentModel(db.Model):
    id = db.Column(db.Integer, db.Sequence('document_model_id_seq'), primary_key=True)
    document_type = db.Column(db.String(50))

    title = db.Column(db.String(256), unique=False, nullable=False)
    body = db.Column(db.Text, nullable=True)
    date_created = db.Column(ArrowType)
    date_modified = db.Column(ArrowType)

    __mapper_args__ = {
        'polymorphic_identity': 'document_model',
        'polymorphic_on': document_type
    }

    def __init__(self, *args, **kwargs):
        # Force the date_created  and date_modified to now.
        kwargs['date_created'] = arrow.utcnow()
        kwargs['date_modified'] = arrow.utcnow()
        super(DocumentModel, self).__init__(*args, **kwargs)
