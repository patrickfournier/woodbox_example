# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from woodbox.db import db
from woodbox.models.user_model import WBUserModel

class UserModel(WBUserModel):
    id = db.Column(db.Integer, db.ForeignKey(WBUserModel.id), primary_key=True)
    name = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'user_model',
    }
