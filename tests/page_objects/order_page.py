import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from data import OrderData, OrderSuccessText

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
    order_success_header = [By.XPATH, '//div[@class= "Order_ModalHeader__3FDaJ" and text() = "Заказ оформлен"]']
    status_check_button = [By.XPATH, '//button[text()="Посмотреть статус"]']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    @allure.step('Ввод имени')
    def set_name(self, data_source):
        name_field = self.wait.until(expected_conditions.element_to_be_clickable(self.name_input))
        name_field.send_keys(OrderData[data_source]["name"])   

    @allure.step('Ввод фамилии')
    def set_surname(self, data_source):
        surname_field = self.wait.until(expected_conditions.element_to_be_clickable(self.surname_input))
        surname_field.send_keys(OrderData[data_source]["surname"])  

    @allure.step('Ввод адреса')
    def set_address(self, data_source):
        address_field = self.wait.until(expected_conditions.element_to_be_clickable(self.address_input))
        address_field.send_keys(OrderData[data_source]["address"])   

    @allure.step('Ввод станции метро')
    def set_subway_station(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.subway_station_select)).click()
        subway_station = self.wait.until(expected_conditions.visibility_of_element_located(self.subway_station_example))
        subway_station.click()   

    @allure.step('Ввод телефона')
    def set_phone(self, data_source):
        phone_field = self.wait.until(expected_conditions.element_to_be_clickable(self.phone_input))
        phone_field.send_keys(OrderData[data_source]["phone"])  

    @allure.step('Переход на следующую страницу')
    def click_next_step_button(self):
        button = self.wait.until(expected_conditions.element_to_be_clickable(self.next_step_button))           
        button.click()       

    @allure.step('Ввод даты доставки')
    def set_delivery_date(self, data_source):
        deliver_date = self.wait.until(expected_conditions.element_to_be_clickable(self.delivery_date))
        deliver_date.send_keys(OrderData[data_source]["delivery_date"])  
        deliver_date.send_keys(Keys.ENTER)      

    @allure.step('Ввод времени аренды')
    def set_rent_time(self):   
        rent_time_select = self.wait.until(expected_conditions.element_to_be_clickable(self.rent_time_select))
        rent_time_select.click()
        rent_time = self.wait.until(expected_conditions.visibility_of_element_located(self.rent_time_example))
        rent_time.click() 

    @allure.step('Выбор цвета')
    def set_color_1(self):
        color_pickup_button = self.wait.until(expected_conditions.element_to_be_clickable(self.black_color_checkbox))
        color_pickup_button.click()

    @allure.step('Выбор цвета')
    def set_color_2(self):
        color_pickup_button = self.wait.until(expected_conditions.element_to_be_clickable(self.grey_color_checkbox))
        color_pickup_button.click()

    @allure.step('Сообщение для курьера')
    def set_comm_for_courier(self, data_source):
        comm_for_courier = self.wait.until(expected_conditions.element_to_be_clickable(self.comm_for_courier))
        comm_for_courier.send_keys(OrderData[data_source]["message"])           

    @allure.step('Подтверждение заказа')
    def click_confirm_order_button(self):
        button = self.wait.until(expected_conditions.element_to_be_clickable(self.confirm_order_button))           
        button.click()     

    @allure.step('Проверка статуса')
    def click_status_check_button(self):
        status_check_button = self.wait.until(expected_conditions.element_to_be_clickable(self.status_check_button))           
        status_check_button.click()   

    @allure.step('Проверка успешного заказа')
    def order_success_message(self):
        order_success_message = self.wait.until(expected_conditions.visibility_of_element_located(self.order_success_header))
        return order_success_message

    @allure.title('Проверка формы заказа с набором данных')
    def check_order_form(self, name, surname, address, phone, delivery_date, message):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_subway_station()
        self.set_phone(phone)
        self.click_next_step_button()
        self.set_delivery_date(delivery_date)
        self.set_rent_time()
        self.set_color_1()
        self.set_comm_for_courier(message)
        self.click_next_step_button()
        self.click_confirm_order_button()
