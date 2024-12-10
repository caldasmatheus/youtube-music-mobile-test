from typing import Tuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_element_by_text(self, text: str, timeout: int = 10):
        try:
            locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            raise Exception(f"Elemento com texto '{text}' não encontrado ou não clicável após {timeout} segundos")
        except Exception as e:
            raise Exception(f"Erro ao clicar no elemento com texto '{text}': {str(e)}")

    def wait_element(self, locator: Tuple[str, str], timeout: int = 10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise Exception(f"Elemento não encontrado após {timeout} segundos: {locator}")
        except Exception as e:
            raise Exception(f"Erro ao localizar o elemento: {str(e)}")

    def is_element_present(self, locator: tuple, timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(*locator)
            )
            return True
        except TimeoutException:
            return False
        except Exception as e:
            raise Exception(f"Erro ao verificar a presença do elemento: {str(e)}")