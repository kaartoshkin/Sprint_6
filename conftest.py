import pytest
from selenium import webdriver
from pages.home_page import HomePageScooter
from pages.base_page import BasePageScooter
from pages.order_page import OrderPageScooter

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def base_page(driver):
    page = BasePageScooter(driver)
    page.open()
    return page

@pytest.fixture
def home_page(driver):
    return HomePageScooter(driver)    

@pytest.fixture
def order_page(driver):
    return OrderPageScooter(driver)