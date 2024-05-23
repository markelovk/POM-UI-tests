import allure
from pages.base_page import BasePage
from locators.order_page_loctors import OrderPageLocators
from locators.main_page_locators import MainPageLocators

class OrderPage(BasePage):
    @allure.step('Заполнение поля Имя')
    def fill_name_field(self, text):
        self.fill_field(OrderPageLocators.field_name, text)

    @allure.step('Заполнение поля Фамилия')
    def fill_surname_field(self,text):
        self.fill_field(OrderPageLocators.field_surname, text)

    @allure.step('Заполнение поля Адресс')
    def fill_adress_field(self,text):
        self.fill_field(OrderPageLocators.field_adress, text)

    @allure.step('Заполнение поля Станция метро')
    def fill_metro_station_field(self, text):
        self.fill_field(OrderPageLocators.field_metro_station, text)
        self.click_element(OrderPageLocators.choose_metro_station)

    @allure.step('Заполнение поля Телефон')
    def fill_telephone_field(self,text):
        self.fill_field(OrderPageLocators.field_telephone, text)

    @allure.step('Нажатие на кнопку Далее')
    def click_button_next(self):
        self.click_element(OrderPageLocators.button_next)
        self.waiting_clickable_element(OrderPageLocators.text_about_rent)

    @allure.step('Заполнение поля Когда привезти самокат')
    def fill_when_bring_scooter(self, text):
        self.click_element(OrderPageLocators.field_when_bring_scooter)
        self.fill_field(OrderPageLocators.field_when_bring_scooter, text)
        self.click_element(OrderPageLocators.date_of_calendar)

    @allure.step('Нажатие на поле выбор срока аренды')
    def click_rental_period(self):
        self.click_element(OrderPageLocators.rental_period)
        self.waiting_clickable_element(OrderPageLocators.choose_rental_period)

    @allure.step('Нажтие на ответ из выпадающего списка поля срока аренды')
    def click_rental_period_time(self):
        self.click_element(OrderPageLocators.choose_rental_period)
        self.waiting_visible_element(OrderPageLocators.field_rental_period)

    @allure.step('Полный цикл выбора срока аренды')
    def choose_rental_period(self):
        self.click_rental_period()
        self.click_rental_period_time()

    @allure.step('Нажатие на кнопку оформления заказа')
    def click_button_middle_order(self):
        self.click_element(OrderPageLocators.middle_button_order)
        self.waiting_visible_element(OrderPageLocators.text_want_order)

    @allure.step('Нажатие кнопки Да при оформлении заказа')
    def click_button_order_yes(self):
        self.click_element(OrderPageLocators.button_yes)
        self.waiting_visible_element(OrderPageLocators.order_completed)

    @allure.step('Нажатие среденй кнопки оформления заказа')
    def click_middle_button_order(self):
        self.click_element(MainPageLocators.middle_button_order)
        self.waiting_visible_element(OrderPageLocators.text_scooter_for)

    @allure.step('Цикл заполнения полей первой страницы заказа')
    def make_scooter_order_page_1(self, data_set):
        self.fill_name_field(data_set[1])
        self.fill_surname_field(data_set[2])
        self.fill_adress_field(data_set[3])
        self.fill_metro_station_field(data_set[4])
        self.fill_telephone_field(data_set[5])
        self.click_button_next()

    @allure.step('Цикл заполнения полей второй страницы заказа')
    def make_scooter_order_page_2(self, data_set):
        self.fill_when_bring_scooter(data_set[6])
        self.choose_rental_period()
        self.click_button_middle_order()

    @allure.step('Получения текста о выполнении заказа')
    def text_order_completed(self):
        return self.text_element(OrderPageLocators.order_completed)