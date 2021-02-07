import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://yandex.ru')
    yield driver
    driver.quit()
