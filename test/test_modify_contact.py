def test_modify_first_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contact.modify_first_contact()
    app.session.logout()