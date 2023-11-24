def test_del_first_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contact.del_first_contact()
    app.session.logout()