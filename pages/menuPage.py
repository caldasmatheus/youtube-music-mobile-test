from pages.basePage import BasePage

class MenuPage(BasePage):

    def go_to_home_page(self):
        self.click_element_by_text("Home")

    def go_to_library_page(self):
        self.click_element_by_text("Library")
