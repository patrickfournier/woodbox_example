# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from datetime import datetime

from woodbox.db import db
from woodbox.models.record_acl_model import RecordACLModel
from woodbox.models.user_model import WBRoleModel

from .models.document_model import DocumentModel
from .models.document_node_model import DocumentNodeModel
from .models.folder_node_model import FolderNodeModel
from .models.node_model import NodeModel
from .models.user_model import UserModel

def populate_db():
    db.initialize()

    anonymous_role_id = WBRoleModel.get_anonymous_role_id()

    admin_role_id = UserModel.get_admin_role_id()
    admin_role = WBRoleModel.query.get(admin_role_id);

    user_role_id = UserModel.get_user_role_id()
    user_role = WBRoleModel.query.get(user_role_id);

    data = {'rolename': 'group1'}
    role = WBRoleModel(**data)
    db.session.add(role)
    db.session.commit()
    group1_role = role

    data = {'rolename': 'group2'}
    role = WBRoleModel(**data)
    db.session.add(role)
    db.session.commit()
    group2_role = role

    data = {'username': "alice", 'password': '123qwe', 'name': "Alice Allard", 'roles': [user_role, group1_role]}
    user = UserModel(**data)
    db.session.add(user)
    db.session.commit()
    alice_id = user.id

    data = {'username': "bob", 'password': '123qwe', 'name': "Bob Binette", 'roles': [user_role, group2_role]}
    user = UserModel(**data)
    db.session.add(user)
    db.session.commit()
    bob_id = user.id

    data = {'username': "charles", 'password': '123qwe', 'name': "Charles Charette", 'roles': [admin_role]}
    user = UserModel(**data)
    db.session.add(user)
    db.session.commit()
    charles_id = user.id

    root_id = FolderNodeModel.get_root_id()

    data = {'title': 'usr', 'parent_node_id': root_id, 'owner_id': alice_id}
    vs = FolderNodeModel(**data)
    db.session.add(vs)

    data = {'title': 'var', 'parent_node_id': root_id, 'owner_id': alice_id}
    vs = FolderNodeModel(**data)
    db.session.add(vs)
    db.session.commit()
    var_id = vs.id

    data = {'title': 'home', 'parent_node_id': root_id, 'owner_id': bob_id}
    vs = FolderNodeModel(**data)
    db.session.add(vs)
    db.session.commit()
    home_id = vs.id

    data = [
        {'record_type': 'ContentNode', 'record_id': home_id, 'user_role_id': anonymous_role_id, 'permission': 'read'},
        {'record_type': 'ContentNode', 'record_id': home_id, 'user_role_id': group1_role.id, 'permission': 'read'},
    ]
    for d in data:
        acl = RecordACLModel(**d)
        db.session.add(acl)
    db.session.commit()

    data = {'title': 'Lorem', 'body': 'Lorem ipsum dolor', 'date_created': datetime.now()}
    vs = DocumentModel(**data)
    db.session.add(vs)
    db.session.commit()

    data = {'document_id': vs.id, 'parent_node_id': home_id, 'owner_id': alice_id}
    doc = DocumentNodeModel(**data)
    db.session.add(doc)
    db.session.commit()

    data = {'title': 'Sit amet', 'body': 'Consectetur adipiscing elit', 'date_created': datetime.now()}
    vs = DocumentModel(**data)
    db.session.add(vs)
    db.session.commit()

    data = {'document_id': vs.id, 'parent_node_id': var_id, 'owner_id': alice_id}
    doc = DocumentNodeModel(**data)
    db.session.add(doc)
    db.session.commit()

    return 'DB Initialization Done'
