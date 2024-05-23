import allure
import pytest
from selenium import webdriver
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Sites

@allure.step('Открытие браузера, переход на страницу самоката, закрытие браузера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Sites.main_page_scooter_url)
    base_page = BasePage(driver)
    base_page.waiting_visible_element(MainPageLocators.text_main_page_scooter)
    yield driver
    driver.quit()