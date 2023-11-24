class GroupHelper:
    def __init__(self, app):
        self.app = app

    def test_add_group(self):
        wd = self.app.wd
        self.login(username="admin", password="secret")
        self.create(Group (name="name", logo="logo", comment="comment"))
        self.logout()

    def test_empty_group(self):
        wd = self.app.wd
        self.login(username="admin", password="secret")
        self.create(Group (name="", logo="", comment=""))
        self.logout()

    def create(self, group):
        #create new group
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.logo)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.comment)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
