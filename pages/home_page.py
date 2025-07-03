import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePageScooter
from locators.home_page_locators import HomePageLocator

class HomePageScooter:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.base_page = BasePageScooter(self.driver)
        
    @allure.step('Клик по верхней кнопке Заказать')    
    def click_upper_order_button(self):
        self.base_page.wait_and_click(HomePageLocator.upper_order_button)  

    @allure.step('Клик по нижней кнопке Заказать')   
    def click_lower_order_button(self):
        self.base_page.wait_and_click(HomePageLocator.lower_order_button)

    @allure.step('Скролл до вопросов')   
    def scroll_to_faq(self):
        self.base_page.scroll_to("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Скролл до нижней кнопки Заказать')      
    def scroll_to_lower_button(self):
        self.base_page.scroll_to("window.scrollTo(0, 2200)")

    @allure.step('Переход на главную')  
    def click_scooter_logo(self):    
        self.base_page.wait_and_click(HomePageLocator.scooter_logo)          

    @allure.step('Переход на дзен')  
    def click_yandex_logo(self):
        self.base_page.wait_and_click(HomePageLocator.yandex_logo) 

    @allure.step('Ожидание загрузки')  
    def wait_for_url_to_change(self):
        self.base_page.url_wait_to_change(self.driver.current_url)

    @allure.step('Вывод {faq_number} вопроса')      
    def click_FAQ(self, faq_number):
        faq_locator = getattr(HomePageLocator, f'FAQ_{faq_number}')
        self.base_page.wait_and_click(faq_locator)

    @allure.step('Ожидание загрузки ответа на вопрос №{faq_number}')
    def wait_for_load_FAQ(self, faq_number: int):
        locator = getattr(HomePageLocator, f"FAQ_{faq_number}_text")
        self.base_page.wait_for_load(locator)

    @allure.step('Проверка {faq_number} вопроса')    
    def check_FAQ(self, faq_number):
        text_locator = getattr(HomePageLocator, f'FAQ_{faq_number}_text')
        faq_text = self.base_page.find_element_on_page(text_locator)
        return faq_text.text