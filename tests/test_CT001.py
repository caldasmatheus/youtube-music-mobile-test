import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from pages.menuPage import MenuPage
from pages.libraryPage import LibraryPage

class TestYouTubeMusic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:deviceName": "Android Emulator",
            "appium:automationName": "UIAutomator2",
            "appium:autoGrantPermissions": True,
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True,
            "appium:appPackage": "com.google.android.apps.youtube.music",
            "appium:appActivity": "com.google.android.apps.youtube.music.activities.MusicActivity"
        })
        cls.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        cls.menu_page = MenuPage(cls.driver)
        cls.library_page = LibraryPage(cls.driver)

    def test_create_playlist(self):
        self.menu_page.go_to_library_page()

        self.library_page.click_new_button()
        self.library_page.click_playlist_option()
        self.library_page.enter_title("Mix")
        self.library_page.enter_description("Playlist de teste")
        self.library_page.select_playlist_option(instance=4)
        self.library_page.select_playlist_option(instance=6)
        self.library_page.create_playlist()

        self.menu_page.go_to_home_page()
        self.menu_page.go_to_library_page()
        self.library_page.select_playlist_menu()
        self.library_page.verify_playlist("Mix")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()