import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base_page import BasePageScooter

class HomePageScooter:
    scooter_logo = [By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]']
    yandex_logo = [By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]']
    upper_order_button = [By.CLASS_NAME,'Button_Button__ra12g']
    lower_order_button = [By.XPATH,'//button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]']
    lower_order_button = [By.XPATH,'//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    order_status_button = [By.CLASS_NAME,'Header_Link__1TAG7']
    FAQ_window = [By.CLASS_NAME, 'Home_FAQ__3uVm4']
    FAQ_1 = [By.ID,'accordion__heading-0']
    FAQ_2 = [By.ID,'accordion__heading-1']
    FAQ_3 = [By.ID,'accordion__heading-2']
    FAQ_4 = [By.ID,'accordion__heading-3']
    FAQ_5 = [By.ID,'accordion__heading-4']
    FAQ_6 = [By.ID,'accordion__heading-5']
    FAQ_7 = [By.ID,'accordion__heading-6']
    FAQ_8 = [By.ID,'accordion__heading-7']
    FAQ_1_text = [By.XPATH, '//*[@id="accordion__panel-0"]/p']
    FAQ_2_text = [By.XPATH, '//*[@id="accordion__panel-1"]/p']
    FAQ_3_text = [By.XPATH, '//*[@id="accordion__panel-2"]/p']
    FAQ_4_text = [By.XPATH, '//*[@id="accordion__panel-3"]/p']
    FAQ_5_text = [By.XPATH, '//*[@id="accordion__panel-4"]/p']
    FAQ_6_text = [By.XPATH, '//*[@id="accordion__panel-5"]/p']
    FAQ_7_text = [By.XPATH, '//*[@id="accordion__panel-6"]/p']
    FAQ_8_text = [By.XPATH, '//*[@id="accordion__panel-7"]/p']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.base_page = BasePageScooter(self.driver)
        
    @allure.step('Клик по верхней кнопке Заказать')    
    def click_upper_order_button(self):
        self.base_page.wait_and_click(*self.upper_order_button)  

    @allure.step('Клик по нижней кнопке Заказать')   
    def click_lower_order_button(self):
        self.base_page.wait_and_click(*self.lower_order_button)

    @allure.step('Скролл до вопросов')   
    def scroll_to_faq(self):
        self.base_page.scroll_to("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Скролл до нижней кнопки Заказать')      
    def scroll_to_lower_button(self):
        self.base_page.scroll_to("window.scrollTo(0, 2200)")

    @allure.step('Переход на главную')  
    def click_scooter_logo(self):    
        self.base_page.wait_and_click(*self.scooter_logo)          

    @allure.step('Переход на дзен')  
    def click_yandex_logo(self):
        self.base_page.wait_and_click(*self.yandex_logo) 

    @allure.step('Ожидание загрузки')  
    def wait_for_url_to_change(self):
        self.base_page.url_wait_to_change(self.driver.current_url)

    @allure.step('Вывод {faq_number} вопроса')      
    def click_FAQ(self, faq_number):
        faq_locator = getattr(self, f'FAQ_{faq_number}')
        self.base_page.wait_and_click(*faq_locator)

    @allure.step('Ожидание загрузки ответа на вопрос №{faq_number}')
    def wait_for_load_FAQ(self, faq_number: int):
        locator = getattr(self, f"FAQ_{faq_number}_text")
        self.base_page.wait_for_load(locator)

    @allure.step('Проверка {faq_number} вопроса')    
    def check_FAQ(self, faq_number):
        text_locator = getattr(self, f'FAQ_{faq_number}_text')
        faq_text = self.base_page.find_element_on_page(*text_locator)
        return faq_text.text