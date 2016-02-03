# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .models.video_sequence_model import FolderNodeModel, DocumentNodeModel, VideoSequenceModel

from woodbox.db import db
from woodbox.models.record_acl_model import RecordACLModel
from woodbox.models.user_model import WBRoleModel

from .models.user_model import UserModel

def populate_db():
    db.drop_all()
    db.create_all()

    data = {'rolename': 'admin'}
    role = WBRoleModel(**data)
    db.session.add(role)
    db.session.commit()
    admin_role = role

    data = {'rolename': 'user'}
    role = WBRoleModel(**data)
    db.session.add(role)
    db.session.commit()
    user_role = role

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

    data = {'title': 'root', 'parent_node_id': None, 'owner_id': alice_id}
    vs = FolderNodeModel(**data)
    db.session.add(vs)
    db.session.commit()
    root_id = vs.id

    data = {'title': 'usr', 'parent_node_id': root_id, 'owner_id': alice_id}
    vs = FolderNodeModel(**data)
    db.session.add(vs)

    data = {'title': 'var', 'parent_node_id': root_id, 'owner_id': alice_id}
    vs = FolderNodeModel(**data)
    db.session.add(vs)

    data = {'title': 'home', 'parent_node_id': root_id, 'owner_id': bob_id}
    vs = FolderNodeModel(**data)
    db.session.add(vs)
    db.session.commit()
    root_id = vs.id

    data = [
        {'record_type': 'ContentNode', 'record_id': root_id, 'user_role': '__anonymous', 'permission': 'read'},
        {'record_type': 'ContentNode', 'record_id': root_id, 'user_role': 'group1', 'permission': 'read'},
    ]
    for d in data:
        acl = RecordACLModel(**d)
        db.session.add(acl)
    db.session.commit()

    data = {'title': 'MyDocument', 'date_unknown': True}
    vs = VideoSequenceModel(**data)
    db.session.add(vs)
    db.session.commit()

    data = {'document_id': vs.id, 'parent_node_id': root_id, 'owner_id': alice_id}
    doc = DocumentNodeModel(**data)
    db.session.add(doc)

    db.session.commit()

    return 'DB Initialization Done'
