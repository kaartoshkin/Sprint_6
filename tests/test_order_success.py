import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from pages.home_page import HomePageScooter
from pages.base_page import BasePageScooter
from pages.order_page import OrderPageScooter
from data import OrderData

class TestOrderSucces:

    @allure.title('Тест заказа через верхнюю кнопку')
    def test_order_with_upper_button(self, home_page, order_page, base_page):

        home_page.click_upper_order_button()
        
        order_page.check_order_form("ORDER_DATA_1")

        assert order_page.order_success_message().is_displayed()

        order_page.click_status_check_button()

        home_page.click_scooter_logo()  
        
        assert base_page.get_current_url() == base_page.base_url 

    @allure.title("Тест заказа через нижнюю кнопку")
    def test_order_with_lower_button(self, home_page, order_page, base_page):

        home_page.scroll_to_lower_button()

        home_page.click_lower_order_button()
        
        order_page.check_order_form("ORDER_DATA_2")

        assert order_page.order_success_message().is_displayed()

        order_page.click_status_check_button()

        home_page.click_scooter_logo()  
        
        assert base_page.get_current_url() == base_page.base_url 

    @allure.title('Тест перехода на дзен')
    def test_logo_redirect(self, home_page, base_page):

        home_page.click_yandex_logo()
        home_page.wait_for_url_to_change()

        assert 'dzen.ru' in base_page.get_current_url()