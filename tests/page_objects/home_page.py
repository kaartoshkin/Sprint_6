import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
        
    @allure.step('Клик по верхней кнопке Заказать')    
    def click_upper_order_button(self):
        self.driver.find_element(*self.upper_order_button).click()   

    @allure.step('Клик по нижней кнопке Заказать')   
    def click_lower_order_button(self):
        self.driver.find_element(*self.lower_order_button).click()   

    @allure.step('Скролл до вопросов')   
    def scroll_to_faq(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Скролл до нижней кнопки Заказать')      
    def scroll_to_lower_button(self):
        self.driver.execute_script("window.scrollTo(0, 2200)")

    @allure.step('Переход на главную')  
    def click_scooter_logo(self):    
        scooter_logo_button = self.wait.until(expected_conditions.element_to_be_clickable(*self.scooter_logo))           
        scooter_logo_button.click()  

    @allure.step('Переход на дзен')  
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()   

    @allure.step('Ожидание загрузки')  
    def wait_for_url_to_change(self):
        self.wait.until(expected_conditions.url_changes(self.driver.current_url))

    @allure.step('Вывод 1 вопроса')      
    def click_FAQ_1(self):
        self.driver.find_element(*self.FAQ_1).click()

    def wait_for_load_FAQ_1(self):
        self.wait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.FAQ_1))

    @allure.step('Проверка 1 вопроса')    
    def check_FAQ_1(self):
        faq_text = self.driver.find_element(*self.FAQ_1_text)
        return faq_text.text
    
    @allure.step('Вывод 2 вопроса')       
    def click_FAQ_2(self):
        self.driver.find_element(*self.FAQ_2).click()  

    def wait_for_load_FAQ_2(self):
        self.wait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.FAQ_2))

    @allure.step('Проверка 2 вопроса')    
    def check_FAQ_2(self):
        faq_text = self.driver.find_element(*self.FAQ_2_text)
        return faq_text.text
    
    @allure.step('Вывод 3 вопроса')        
    def click_FAQ_3(self):
        self.driver.find_element(*self.FAQ_3).click()  

    def wait_for_load_FAQ_3(self):
        self.wait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.FAQ_3))

    @allure.step('Проверка 3 вопроса')    
    def check_FAQ_3(self):
        faq_text = self.driver.find_element(*self.FAQ_3_text)
        return faq_text.text

    @allure.step('Вывод 4 вопроса')     
    def click_FAQ_4(self):
        self.driver.find_element(*self.FAQ_4).click()   

    def wait_for_load_FAQ_4(self):
        self.wait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.FAQ_4))

    @allure.step('Проверка 4 вопроса')    
    def check_FAQ_4(self):
        faq_text = self.driver.find_element(*self.FAQ_4_text)
        return faq_text.text

    @allure.step('Вывод 5 вопроса')     
    def click_FAQ_5(self):
        self.driver.find_element(*self.FAQ_5).click()  

    def wait_for_load_FAQ_5(self):
        self.wait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.FAQ_5))

    @allure.step('Проверка 5 вопроса')    
    def check_FAQ_5(self):
        faq_text = self.driver.find_element(*self.FAQ_5_text)
        return faq_text.text
    
    @allure.step('Вывод 6 вопроса')     
    def click_FAQ_6(self):
        self.driver.find_element(*self.FAQ_6).click()  

    def wait_for_load_FAQ_6(self):
        self.wait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.FAQ_6))

    @allure.step('Проверка 6 вопроса')    
    def check_FAQ_6(self):
        faq_text = self.driver.find_element(*self.FAQ_6_text)
        return faq_text.text

    @allure.step('Вывод 7 вопроса') 
    def click_FAQ_7(self):
        self.driver.find_element(*self.FAQ_7).click() 

    def wait_for_load_FAQ_7(self):
        self.wait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.FAQ_7))

    @allure.step('Проверка 7 вопроса')    
    def check_FAQ_7(self):
        faq_text = self.driver.find_element(*self.FAQ_7_text)
        return faq_text.text
    
    @allure.step('Вывод 8 вопроса')        
    def click_FAQ_8(self):
        self.driver.find_element(*self.FAQ_8).click() 

    def wait_for_load_FAQ_8(self):
        self.wait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.FAQ_8))

    @allure.step('Проверка 8 вопроса')             
    def check_FAQ_8(self):
        faq_text = self.driver.find_element(*self.FAQ_8_text)
        return faq_text.text