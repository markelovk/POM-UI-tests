import allure
from data import Sites
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.logo_locators import LogoLocators

class MainPage(BasePage):
    @allure.step('Прокрутка страницы до раздела с FAQ')
    def scroll_to_faq(self):
        self.scroll_page(MainPageLocators.question_how_much_is_this)
        self.waiting_clickable_element(MainPageLocators.question_how_much_is_this)

    @allure.step('Нажатие на вопрос')
    def click_question_how_much_is_this(self):
        self.click_element(MainPageLocators.question_how_much_is_this)
        self.waiting_visible_element(MainPageLocators.answer_how_much_is_this)

    @allure.step('Нажатие на вопрос')
    def click_question_want_any_scooters(self):
        self.click_element(MainPageLocators.question_want_any_scooters)
        self.waiting_visible_element(MainPageLocators.answer_want_any_scooters)

    @allure.step('Нажатие на вопрос')
    def click_question_how_calculate_rent_time(self):
        self.click_element(MainPageLocators.question_how_calculate_rent_time)
        self.waiting_visible_element(MainPageLocators.answer_how_calculate_rent_time)

    @allure.step('Нажатие на вопрос')
    def click_question_can_scooter_order_today(self):
        self.click_element(MainPageLocators.question_can_scooter_order_today)
        self.waiting_visible_element(MainPageLocators.answer_can_scooter_order_today)

    @allure.step('Нажатие на вопрос')
    def click_question_can_extend_or_return_scooter_before(self):
        self.click_element(MainPageLocators.question_can_extend_or_return_scooter_before)
        self.waiting_visible_element(MainPageLocators.answer_can_extend_or_return_scooter_before)

    @allure.step('Нажатие на вопрос')
    def click_question_bring_charger_with_scooter(self):
        self.click_element(MainPageLocators.question_bring_charger_with_scooter)
        self.waiting_visible_element(MainPageLocators.answer_bring_charger_with_scooter)

    @allure.step('Нажатие на вопрос')
    def click_question_can_cancell_order(self):
        self.click_element(MainPageLocators.question_can_cancell_order)
        self.waiting_visible_element(MainPageLocators.answer_can_cancell_order)

    @allure.step('Нажатие на вопрос')
    def click_question_bring_outside_mkad(self):
        self.click_element(MainPageLocators.question_bring_outside_mkad)
        self.waiting_visible_element(MainPageLocators.answer_bring_outside_mkad)

    @allure.step('Получение текста ответа')
    def text_answer_how_much_is_this(self):
        return self.text_element(MainPageLocators.answer_how_much_is_this)

    @allure.step('Получение текста ответа')
    def text_answer_want_any_scooters(self):
        return self.text_element(MainPageLocators.answer_want_any_scooters)

    @allure.step('Получение текста ответа')
    def text_answer_how_calculate_rent_time(self):
        return self.text_element(MainPageLocators.answer_how_calculate_rent_time)

    @allure.step('Получение текста ответа')
    def text_answer_can_scooter_order_today(self):
        return self.text_element(MainPageLocators.answer_can_scooter_order_today)

    @allure.step('Получение текста ответа')
    def text_answer_can_extend_or_return_scooter_before(self):
        return self.text_element(MainPageLocators.answer_can_extend_or_return_scooter_before)

    @allure.step('Получение текста ответа')
    def text_answer_bring_charger_with_scooter(self):
        return self.text_element(MainPageLocators.answer_bring_charger_with_scooter)

    @allure.step('Получение текста ответа')
    def text_answer_can_cancell_order(self):
        return self.text_element(MainPageLocators.answer_can_cancell_order)

    @allure.step('Получение текста ответа')
    def text_answer_bring_outside_mkad(self):
        return self.text_element(MainPageLocators.answer_bring_outside_mkad)

    @allure.step('Нажатие на логотип Самоката')
    def click_logo_scooter(self):
        self.click_element(LogoLocators.button_logo_scooter)
        self.waiting_visible_element(MainPageLocators.text_main_page_scooter)

    @allure.step('Нажатие на логотип Яндекса')
    def click_logo_yandex(self):
        self.click_element(LogoLocators.button_logo_dzen)
        self.switch_to_new_tab()
        self.waiting_to_be_element(Sites.yandex_url)
