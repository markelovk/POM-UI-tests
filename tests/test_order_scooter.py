import allure
from conftest import driver
from pages.order_page import OrderPage
from data import DataSet, Data


class TestOrderScooter():
    @allure.title('Тестирование оформления заказа при нажатии кнопки заказа в шапке главной страницы сайта')
    @allure.description('Проверка перехода на страницу оформления заказа при нажатии на кнопку Заказать из шапки главной страницы сайта'
                        'И дальнейшее заполнения данных на двух страницах до появления всплывающего окна с сообщением об успешном создании заказа')
    def test_order_by_button_in_the_header(self, driver):
        order_page = OrderPage(driver)
        order_page.accept_cookie()
        order_page.click_button_order()
        order_page.make_scooter_order_page_1(DataSet.data_set_1)
        order_page.make_scooter_order_page_2(DataSet.data_set_1)
        order_page.click_button_order_yes()
        text = order_page.text_order_completed()
        assert text == Data.order_completed

    @allure.title('Тестирование оформления заказа при нажатии кнопки заказа в середине главной страницы сайта')
    @allure.description('Проверка перехода на страницу оформления заказа при нажатии на кнопку Заказать в середине главной страницы сайта'
                        'И дальнейшее заполнения данных на двух страницах до появления всплывающего окна с сообщением об успешном создании заказа')
    def test_order_by_button_in_the_middle(self, driver):
        order_page = OrderPage(driver)
        order_page.accept_cookie()
        order_page.click_middle_button_order()
        order_page.make_scooter_order_page_1(DataSet.data_set_2)
        order_page.make_scooter_order_page_2(DataSet.data_set_2)
        order_page.click_button_order_yes()
        text = order_page.text_order_completed()
        assert text == Data.order_completed
