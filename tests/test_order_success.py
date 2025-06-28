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

class TestOrderSucces:

    @allure.title('Тест заказа через верхнюю кнопку')
    def test_order_with_upper_button(self):

        self.home_page.click_upper_order_button()
        
        self.order_page.check_order_form(OrderData.ORDER_DATA_1['name'], 
                                        OrderData.ORDER_DATA_1['surname'], 
                                        OrderData.ORDER_DATA_1['address'],
                                        OrderData.ORDER_DATA_1['phone'],
                                        OrderData.ORDER_DATA_1['delivery_date'],
                                        OrderData.ORDER_DATA_1['message'])

        self.order_page.click_status_check_button()

        assert self.order_page.order_success_message.is_displayed

        self.home_page.click_scooter_logo()  
        
        assert self.driver.current_url == self.home_page.base_url 

    @allure.title('Тест заказа через нижнюю кнопку')
    def test_order_with_lower_button(self):

        self.home_page.click_upper_order_button()
        
        self.order_page.check_order_form(OrderData.ORDER_DATA_2['name'], 
                                        OrderData.ORDER_DATA_2['surname'], 
                                        OrderData.ORDER_DATA_2['address'],
                                        OrderData.ORDER_DATA_2['phone'],
                                        OrderData.ORDER_DATA_2['delivery_date'],
                                        OrderData.ORDER_DATA_2['message'])

        self.order_page.click_status_check_button()

        assert self.order_page.order_success_message.is_displayed

        self.home_page.click_scooter_logo()  
        
        assert self.base_page.get_current_url == self.home_page.base_url 

    @allure.title('Тест перехода на дзен')
    def test_logo_redirect(self):

        self.home_page.click_yandex_logo()
        self.home_page.wait_for_url_to_change

        assert 'dzen.ru' in self.driver.current_url