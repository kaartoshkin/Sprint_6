import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from page_objects.home_page import HomePageScooter
from page_objects.tst_order_page import OrderPageScooter
from page_objects.base_page import BasePageScooter
from data import OrderData

@pytest.fixture(autouse=True)
def setup(self):
    self.driver = webdriver.Firefox()
    self.base_page = BasePageScooter(self.driver)
    self.home_page = HomePageScooter(self.driver)
    self.base_page.open()
    self.home_page.scroll_to_faq()
    yield self.driver, self.base_page, self.home_page
    self.driver.quit()
