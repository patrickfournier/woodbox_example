# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .models.video_sequence_model import FolderNodeModel, DocumentNodeModel, VideoSequenceModel

from woodbox.db import db
from woodbox.models.user_model import UserModel

def populate_db():
    db.drop_all()
    db.create_all()

    data = {'username': "alice", 'password': '123qwe', 'name': "Alice Allard"}
    user = UserModel(**data)
    db.session.add(user)
    db.session.commit()
    alice_id = user.id

    data = {'username': "bob", 'password': '123qwe', 'name': "Bob Binette"}
    user = UserModel(**data)
    db.session.add(user)
    db.session.commit()
    bob_id = user.id

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

    data = {'title': 'MyDocument', 'date_unknown': True}
    vs = VideoSequenceModel(**data)
    db.session.add(vs)
    db.session.commit()

    data = {'document_id': vs.id, 'parent_node_id': root_id, 'owner_id': alice_id}
    doc = DocumentNodeModel(**data)
    db.session.add(doc)

    db.session.commit()

    return 'DB Initialization Done'
