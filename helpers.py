from selenium import webdriver


def switch_to_tab(driver: webdriver, tab_number: int):
    driver.switch_to.window(driver.window_handles[int(tab_number)-1])
