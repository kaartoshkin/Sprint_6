import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from page_objects.home_page import HomePageScooter
from page_objects.order_page import OrderPageScooter
from page_objects.base_page import BasePageScooter

class TestOrderSucces:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Firefox()
        self.base_page = BasePageScooter(self.driver)
        self.home_page = HomePageScooter(self.driver)
        self.order_page = OrderPageScooter(self.driver)
        self.base_page.open()
        yield self.driver, self.base_page, self.home_page
        self.driver.quit()

    @allure.title('Тест заказа через верхнюю кнопку')
    def test_order_with_upper_button(self):

        self.home_page.click_upper_order_button()
        
        self.order_page.check_order_form_1()

        self.order_page.click_status_check_button()

        self.home_page.click_scooter_logo()  
        
        assert self.driver.current_url == self.home_page.base_url 

    @allure.title('Тест заказа через нижнюю кнопку')
    def test_order_with_lower_button(self):

        self.home_page.click_upper_order_button()
        
        self.order_page.check_order_form_2()

        self.order_page.click_status_check_button()

        self.home_page.click_scooter_logo()  
        
        assert self.driver.current_url == self.home_page.base_url 

    @allure.title('Тест перехода на дзен')
    def test_logo_redirect(self):

        self.home_page.click_yandex_logo()
        self.home_page.wait_for_url_to_change

        assert 'dzen.ru' in self.driver.current_url