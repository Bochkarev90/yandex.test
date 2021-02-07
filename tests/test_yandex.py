from page_objects import MainPage, ResultPage, PicturePage


def test_1_perfect_art_page(driver):
    first_result = MainPage(driver).put_text_in_search_field('perfect art').click_search_button()[1]
    assert first_result.link == 'perfectart.ru'
    first_result.choose()
    assert ResultPage(driver).link == 'https://perfectart.ru/'


def test_2_pictures(driver):
    first_picture_link = MainPage(driver).choose_service('Картинки').choose_topic_number(1).expand_picture_number(2).\
        get_picture_link()
    second_picture_link = PicturePage(driver).open_next_picture().get_picture_link()
    third_picture_link = PicturePage(driver).open_previous_picture().get_picture_link()
    assert first_picture_link != second_picture_link
    assert first_picture_link == third_picture_link
