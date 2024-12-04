from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys

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
        self.wait_element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("Add a song")'))

    def select_playlist_menu(self):
        self.click_element_by_text("Playlists")

    def verify_playlist(self, playlist_name):
        element_playlist = self.wait_element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{playlist_name}")'))
        return element_playlist

    def playlist_options(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().resourceId(\"com.google.android.apps.youtube.music:id/contextual_menu_anchor\").instance(1)").click()

    def click_delete_playlist(self):
        self.click_element_by_text("Delete playlist")

    def confirm_delete_playlist(self):
        self.wait_element((AppiumBy.ID, "android:id/button1")).click()

    def select_playlist(self, playlist_name):
        self.click_element_by_text(playlist_name)

    def click_add_a_song(self):
        self.click_element_by_text("Add a song")

    def search_song(self):
        song = self.wait_element((AppiumBy.ID, "com.google.android.apps.youtube.music:id/search_edit_text"))
        song.click()
        song.send_keys("musicas sertanejas")
        self.wait_element((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.google.android.apps.youtube.music:id/search_type_icon\").instance(0)")).click()

    def add_song_in_playlist(self):
        add_song = self.wait_element((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.google.android.apps.youtube.music:id/two_column_item_highlight\").instance(0)"))
        add_song.click()

    def verify_song_in_playlist(self):
        song_element = self.wait_element((AppiumBy.ID, "com.google.android.apps.youtube.music:id/message_subtext"))
        song_text = song_element.text
        return song_text

    def click_edit_playlist(self):
        self.wait_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Edit playlist")')).click()

    def enter_new_title(self, title):
        new_title = self.wait_element((AppiumBy.ACCESSIBILITY_ID, "Title"))
        new_title.clear()
        new_title.send_keys(title)

    def enter_new_description(self, description):
        new_description = self.wait_element((AppiumBy.ACCESSIBILITY_ID, "Description (optional)"))
        new_description.clear()
        new_description.send_keys(description)

    def click_done(self):
        self.wait_element((AppiumBy.ID, "com.google.android.apps.youtube.music:id/done_editing")).click()
        
    def remove_music_song(self):
        self.wait_element((AppiumBy.ACCESSIBILITY_ID, "Menu")).click()
        
    def remove_confirm_music(self):
        self.wait_element((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Remove from playlist\")")).click()
