import pytest
from selenium import webdriver

from config import headless


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    if bool(headless):
        options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://yandex.ru')
    yield driver
    driver.quit()
