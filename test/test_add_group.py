# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group (name="name", logo="logo", comment="comment"))
        app.session.logout()
def test_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group (name="", logo="", comment=""))
        app.session.logout()

