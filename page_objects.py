from selenium import webdriver

from helpers import switch_to_tab
from page_elements import Button, WaitingElement


class _BasePage:

    def __init__(self, driver: webdriver):
        self._driver = driver


class MainPage(_BasePage):

    @property
    def search_field(self):
        return WaitingElement(self._driver, 'input#text')

    @property
    def search_button(self):
        return Button(self._driver, 'Найти')

    def put_text_in_search_field(self, text: str):
        self.search_field.send_keys(str(text))
        return self

    def click_search_button(self):
        self.search_button.click()
        return SearchPage(self._driver)

    def choose_service(self, service_title: str):
        _ServiceIcon(self._driver, service_title).click()
        switch_to_tab(self._driver, 2)
        return TopicPage(self._driver)


class _ServiceIcon(WaitingElement):

    def __init__(self, driver: webdriver, icon_text: str):
        super().__init__(driver, f'//div[@class="services-new__item-title"][normalize-space()="{str(icon_text)}"]')


class SearchPage:

    def __init__(self, driver: webdriver):
        self._driver = driver
        self._results = [_SearchResult(self._driver, i+1) for i in range(10)]

    def __getitem__(self, item: int):
        return self._results[int(item) - 1]

    def open_search_result_number(self, index: int = 1):
        return self[index].choose()


class _SearchResult(WaitingElement):

    def __init__(self, driver: webdriver, index: int):
        super().__init__(driver, f'//li[@class="serp-item"][{int(index)}]')
        self._title_element = self.find_element_by_css_selector('h2')
        self._link_element = self.find_element_by_xpath('//a[contains(@class, "link")]/b')

    @property
    def title(self):
        return self._title_element.text

    @property
    def link(self):
        return self._link_element.text

    def choose(self):
        self._link_element.click()
        switch_to_tab(self._driver, 2)
        return ResultPage(self._driver)


class ResultPage(_BasePage):

    @property
    def link(self):
        return self._driver.current_url


class TopicPage(_BasePage):

    def __getitem__(self, item: int):
        return _Topic(self._driver, int(item) - 1)

    def choose_topic_number(self, topic_number: int):
        self[topic_number].click()
        return PicturePage(self._driver)


class _Topic(WaitingElement):

    def __init__(self, driver: webdriver, topic_number: int):
        super().__init__(driver, f'div.PopularRequestList-Item_pos_{int(topic_number)}')


class PicturePage(_BasePage):

    def __getitem__(self, item: int):
        return _PicturePreview(self._driver, int(item) - 1)

    @property
    def picture_element(self):
        return WaitingElement(self._driver, 'img.MMImage-Origin')

    @property
    def previous_button_element(self):
        return WaitingElement(self._driver, 'div.CircleButton_type_prev i')

    @property
    def next_button_element(self):
        return WaitingElement(self._driver, 'div.CircleButton_type_next i')

    def expand_picture_number(self, picture_num: int):
        self[picture_num].click()
        return self

    def get_picture_link(self):
        return self.picture_element.get_attribute('src')

    def open_previous_picture(self):
        self.previous_button_element.click()
        return PicturePage(self._driver)

    def open_next_picture(self):
        self.next_button_element.click()
        return PicturePage(self._driver)


class _PicturePreview(WaitingElement):

    def __init__(self, driver: webdriver, picture_number: int):
        super().__init__(driver, f'div.serp-item_pos_{int(picture_number)}')
