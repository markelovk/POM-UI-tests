import allure
import pytest
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver
from data import Data, Sites


class TestMainPage():
    @allure.title('Тестирование раскрывающегося списка с FAQ')
    @allure.description('Проверка раскрытия вопроса при нажатии и правильности ответов на эти вопросы')
    @pytest.mark.parametrize("click_method, answer_method, expected_text", [
        (MainPage.click_question_how_much_is_this, MainPage.text_answer_how_much_is_this, Data.answer_how_much_is_this),
        (MainPage.click_question_want_any_scooters, MainPage.text_answer_want_any_scooters,
         Data.answer_want_any_scooters),
        (MainPage.click_question_how_calculate_rent_time, MainPage.text_answer_how_calculate_rent_time,
         Data.answer_how_calculate_rent_time),
        (MainPage.click_question_can_scooter_order_today, MainPage.text_answer_can_scooter_order_today,
         Data.answer_can_scooter_order_today),
        (MainPage.click_question_can_extend_or_return_scooter_before,
         MainPage.text_answer_can_extend_or_return_scooter_before, Data.answer_can_extend_or_return_scooter_before),
        (MainPage.click_question_bring_charger_with_scooter, MainPage.text_answer_bring_charger_with_scooter,
         Data.answer_bring_charger_with_scooter),
        (MainPage.click_question_can_cancell_order, MainPage.text_answer_can_cancell_order,
         Data.answer_can_cancell_order),
        (MainPage.click_question_bring_outside_mkad, MainPage.text_answer_bring_outside_mkad,
         Data.answer_bring_outside_mkad),
    ])
    def test_click_questions(self, driver, click_method, answer_method, expected_text):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.scroll_to_faq()
        click_method(main_page)
        text = answer_method(main_page)
        assert text == expected_text

    @allure.title('Тестирование перехода при клике по логотипу Самокат')
    @allure.description('Проверка перехода на главную страницу Самоката при клике на логотип ')
    def test_click_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_button_order()
        main_page.click_logo_scooter()
        current_url = main_page.check_page_current_url()
        assert current_url == Sites.main_page_scooter_url

    @allure.title('Тестирование перехода при клике по логотипу Яндекс')
    @allure.description('Проверка перехода на главную страницу Яндекс Дзена при клике на логотип ')
    def test_click_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        WW(driver, 20).until(ec.url_to_be(Sites.yandex_url))
        current_url = main_page.check_page_current_url()
        assert current_url == Sites.yandex_url
