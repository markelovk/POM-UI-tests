import allure
import pytest
from selenium import webdriver
from data import Sites

@allure.step('Открытие браузера, переход на страницу самоката, закрытие браузера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Sites.main_page_scooter_url)
    yield driver
    driver.quit()