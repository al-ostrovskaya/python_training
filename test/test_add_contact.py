# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.session.login("admin", "secret")
        app.contact.add(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                nickname="nickname", title="title", company="company", address="address",
                                home="12", mobile="34",
                                work="56", fax="78", email="a@a.com", email2="a@a.com", email3="a@a.com",
                                homepage="http://111.ru",
                                byear="1990", ayear="2020", address2="address2", phone2="home2", notes="notes"))
        app.session.logout()



