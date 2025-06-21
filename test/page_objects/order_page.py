from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPageScooter:
    order_header = [By.CLASS_NAME, 'Order_Header__BZXOb']
    name_input = [By.XPATH,'//input[@placeholder="* Имя"]']
    surname_input = [By.XPATH,'//input[@placeholder="* Фамилия"]']
    address_input = [By.XPATH,'//input[@placeholder="* Адрес: куда привезти заказ"]']
    subway_station_select = [By.CLASS_NAME,'select-search__input']
    subway_station_example = [By.CLASS_NAME, 'Order_Text__2broi']
    phone_input = [By.XPATH,'//input[@placeholder="* Телефон: на него позвонит курьер"]']
    delivery_date = [By.XPATH,'//input[@placeholder="* Когда привезти самокат"]']
    rent_time_select = [By.CLASS_NAME, 'Dropdown-root']
    rent_time_example = [By.XPATH, '//div[@class="Dropdown-option" and text() = "сутки"]']
    black_color_checkbox = [By.ID, 'black']
    grey_color_checkbox = [By.ID, 'grey']
    comm_for_courier = [By.XPATH, '//input[@class = "Input_Input__1iN_Z Input_Responsible__1jDKN"]']
    next_step_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    confirm_order_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Да"]']
    order_succes_header = [By.XPATH, '//div[@class= "Order_ModalHeader__3FDaJ" and text() = "Заказ оформлен"]']
    status_check_button = [By.XPATH, '//button[text()="Посмотреть статус"]']

    ORDER_DATA_1 = {
            "name": "Иван",
            "surname": "Иванов",
            "address": "Москва, ул. Пушкина, 999",
            "phone": "+79876543210",
            "delivery_date": "12.12.2025",
            "message": "Привет"
            }

    ORDER_DATA_2 = {
            "name": "Мария",
            "surname": "Иванова",
            "address": "Москва, ул. Есенина, 111",
            "phone": "+71234567890",
            "delivery_date": "11.11.2025",
            "message": "Привет!!!"
            }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def set_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)       

    def set_surname(self, surname):
        self.driver.find_element(*self.surname_input).send_keys(surname)     

    def set_adress(self, adress):
        self.driver.find_element(*self.adress_input).send_keys(adress)   

    def set_subway_station(self):
        self.driver.find_element(*self.subway_station_select).click()
        