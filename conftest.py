import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from pages.menuPage import MenuPage
from pages.libraryPage import LibraryPage
from utils.utils import take_screenshot

def pytest_addoption(parser):
    parser.addoption("--device", default='Android Emulator', help='Select device to run tests.')

@pytest.fixture(scope="function")
def appium_driver(request):
    device = request.config.getoption('device')
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": device,
        "appium:automationName": "UIAutomator2",
        "appium:autoGrantPermissions": True,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:appPackage": "com.google.android.apps.youtube.music",
        "appium:appActivity": "com.google.android.apps.youtube.music.activities.MusicActivity"
    })
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    yield driver
    take_screenshot(driver, request.node.name)
    driver.quit()

@pytest.fixture
def open_app(appium_driver):
    menu_page = MenuPage(appium_driver)
    library_page = LibraryPage(appium_driver)
    yield menu_page, library_page

@pytest.fixture
def navigate_to_home(open_app):
    menu_page = open_app
    yield menu_page

@pytest.fixture
def navigate_to_library(open_app):
    menu_page, library_page = open_app
    menu_page.go_to_library_page()
    yield menu_page, library_page