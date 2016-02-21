# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from sqlalchemy.ext.declarative import declared_attr

from woodbox.access_control.record import RecordACLModel
from woodbox.models.user_model import WBRoleModel
from woodbox.db import db, DatabaseInitializer

from .node_model import NodeModel
from .user_model import UserModel, UserModelInitializer

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

    _root_id = None
    @classmethod
    def get_root_id(cls):
        """Return the root node id."""
        if cls._root_id is None:
            root = FolderNodeModel.query.filter_by(title='root').order_by(FolderNodeModel.id).first()
            cls._root_id = root.id
        return cls._root_id


class FolderNodeModelInitializer(DatabaseInitializer):
    dependencies = [UserModelInitializer]

    """Database initializer for folders: insert the root folder."""
    @staticmethod
    def do_init():
        root = FolderNodeModel(title='root', owner_id=UserModel.get_admin_id(), parent_node_id=None)
        db.session.add(root)
        db.session.commit()

        acl = RecordACLModel(record_type='ContentNode',
                             record_id=root.id,
                             user_role_id=UserModel.get_user_role_id(),
                             permission='read')
        db.session.add(acl)
        db.session.commit()
