from appium.webdriver.common.appiumby import AppiumBy

from pages.basePage import BasePage

class LibraryPage(BasePage):

    def click_new_button(self):
        self.click_element_by_text("New")

    def click_playlist_option(self):
        self.click_element_by_text("Playlist")

    def enter_title(self, title):
        title_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Title")')
        title_field.click()
        title_field.send_keys(title)

    def enter_description(self, description):
        description_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Description")')
        description_field.click()
        description_field.send_keys(description)

    def select_playlist_option(self, instance):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("android.view.ViewGroup").instance({instance})').click()

    def create_playlist(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create").click()

    def select_playlist_menu(self):
        self.click_element_by_text("Playlists")

    def verify_playlist(self, playlist_name):
        element_playlist = self.wait_element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{playlist_name}")'))
        return element_playlist