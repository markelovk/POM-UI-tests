import allure
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec
from locators.main_page_locators import MainPageLocators
from locators.order_page_loctors import OrderPageLocators

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    @allure.step('Прокрутка страницы до элемента')
    def scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик на элемент')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получение текста элемента')
    def text_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Ожидание видимости элемента')
    def waiting_visible_element(self, locator):
        WW(self.driver, 20).until(ec.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def waiting_clickable_element(self, locator):
        WW(self.driver, 10).until(ec.element_to_be_clickable(locator))

    @allure.step('Нажатие на кнопку принятия куки')
    def accept_cookie(self):
        self.click_element(MainPageLocators.button_accept_cookie)

    @allure.step('Заполнение поля')
    def fill_field(self,locator,text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Нажатие кнопки Заказать')
    def click_button_order(self):
        self.click_element(MainPageLocators.upper_button_order)
        self.waiting_visible_element(OrderPageLocators.text_scooter_for)

    @allure.step('Переход на новое окно')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверка url')
    def check_page_current_url(self):
        return self.driver.current_url