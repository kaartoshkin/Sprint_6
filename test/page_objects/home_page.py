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
    check_FAQ_1 = [By.ID,'accordion__heading-0']
    check_FAQ_2 = [By.ID,'accordion__heading-1']
    check_FAQ_3 = [By.ID,'accordion__heading-2']
    check_FAQ_4 = [By.ID,'accordion__heading-3']
    check_FAQ_5 = [By.ID,'accordion__heading-4']
    check_FAQ_6 = [By.ID,'accordion__heading-5']
    check_FAQ_7 = [By.ID,'accordion__heading-6']
    check_FAQ_8 = [By.ID,'accordion__heading-7']
    FAQ_1_text = [By.XPATH, '//*[@id="accordion__panel-0"]/p']
    FAQ_2_text = [By.XPATH, '//*[@id="accordion__panel-1"]/p']
    FAQ_3_text = [By.XPATH, '//*[@id="accordion__panel-2"]/p']
    FAQ_4_text = [By.XPATH, '//*[@id="accordion__panel-3"]/p']
    FAQ_5_text = [By.XPATH, '//*[@id="accordion__panel-4"]/p']
    FAQ_6_text = [By.XPATH, '//*[@id="accordion__panel-5"]/p']
    FAQ_7_text = [By.XPATH, '//*[@id="accordion__panel-6"]/p']
    FAQ_8_text = [By.XPATH, '//*[@id="accordion__panel-7"]/p']
    correct_FAQ_1_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    correct_FAQ_2_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.' 
    correct_FAQ_3_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    correct_FAQ_4_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    correct_FAQ_5_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    correct_FAQ_6_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    correct_FAQ_7_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    correct_FAQ_8_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        
    def click_upper_order_button(self):
        self.driver.find_element(*self.upper_order_button).click()   

    def click_lower_order_button(self):
        self.driver.find_element(*self.lower_order_button).click()   

    def scroll_to_faq(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_lower_button(self):
        self.driver.execute_script("window.scrollTo(0, 2200)")

    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()      

    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()   

    def click_FAQ_1(self):
        self.driver.find_element(*self.check_FAQ_1).click()        

    def click_FAQ_2(self):
        self.driver.find_element(*self.check_FAQ_2).click()  

    def click_FAQ_3(self):
        self.driver.find_element(*self.check_FAQ_3).click()  

    def click_FAQ_4(self):
        self.driver.find_element(*self.check_FAQ_4).click()   

    def click_FAQ_5(self):
        self.driver.find_element(*self.check_FAQ_5).click()  

    def click_FAQ_6(self):
        self.driver.find_element(*self.check_FAQ_6).click()  

    def click_FAQ_7(self):
        self.driver.find_element(*self.check_FAQ_7).click() 

    def click_FAQ_8(self):
        self.driver.find_element(*self.check_FAQ_8).click()     
