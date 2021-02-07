from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import timeout


class WaitingElement:

    def __init__(self, driver: webdriver, xpath_or_css: str):
        self._driver = driver
        self._locator = xpath_or_css

    def _searcher(self):
        if self._locator.startswith('/'):
            return self._driver.find_element_by_xpath(self._locator)
        else:
            return self._driver.find_element_by_css_selector(self._locator)

    def __getattr__(self, item):
        if self._locator.startswith('/'):
            WebDriverWait(self._driver, int(timeout)).until(
                EC.presence_of_element_located((By.XPATH, self._locator)))
        else:
            WebDriverWait(self._driver, int(timeout)).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self._locator)))
        return getattr(self._searcher(), item)


class Button(WaitingElement):

    def __init__(self, driver: webdriver, button_text: str):
        super().__init__(driver, f'//button[normalize-space()="{str(button_text)}"]')
