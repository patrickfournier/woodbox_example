# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from woodbox.db import db, DatabaseInitializer
from woodbox.models.user_model import WBRoleModel, WBUserModel

class UserModel(WBUserModel):
    id = db.Column(db.Integer, db.ForeignKey(WBUserModel.id), primary_key=True)
    name = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'user_model',
    }

    _admin_id = None
    _admin_role_id = None
    _user_role_id = None

    @classmethod
    def get_admin_id(cls):
        """Return the admin id."""
        if cls._admin_id is None:
            admin = UserModel.query.filter_by(username='admin').first()
            cls._admin_id = admin.id
        return cls._admin_id

    @classmethod
    def get_admin_role_id(cls):
        """Return the admin role id."""
        if cls._admin_role_id is None:
            admin_role = WBRoleModel.query.filter_by(rolename='administrator').first()
            cls._admin_role_id = admin_role.id
        return cls._admin_role_id

    @classmethod
    def get_user_role_id(cls):
        """Return the user role id."""
        if cls._user_role_id is None:
            user_role = WBRoleModel.query.filter_by(rolename='user').first()
            cls._user_role_id = user_role.id
        return cls._user_role_id



class UserModelInitializer(DatabaseInitializer):
    """Database initializer for roles: insert the anonymous role."""
    @staticmethod
    def do_init():
        user_role = WBRoleModel(rolename='user')
        db.session.add(user_role)
        db.session.commit()

        admin_role = WBRoleModel(rolename='administrator')
        db.session.add(admin_role)
        db.session.commit()

        admin = UserModel(username='admin', name='Site Administrator', password='admin', roles=[admin_role])
        db.session.add(admin)
        db.session.commit()
