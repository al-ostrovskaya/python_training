def test_modify_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact()
    app.session.logout()