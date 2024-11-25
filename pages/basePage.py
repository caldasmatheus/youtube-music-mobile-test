from typing import Tuple

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_element_by_text(self, text: str, timeout: int = 10):
        try:
            locator = f'new UiSelector().text("{text}")'
            element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locator)
            self.driver.implicitly_wait(timeout)
            element.click()
        except Exception as e:
            raise Exception(f"Erro ao clicar no elemento com texto '{text}': {str(e)}")

    def wait_element(self, locator: Tuple[str, str], timeout: int = 10):
        self.driver.implicitly_wait(timeout)
        try:
            return self.driver.find_element(*locator)
        except Exception as e:
            raise Exception(f"Elemento não encontrado após {timeout} segundos: {str(e)}")

    def is_element_present(self, locator: tuple, timeout: int = 10) -> bool:
        self.driver.implicitly_wait(timeout)
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False