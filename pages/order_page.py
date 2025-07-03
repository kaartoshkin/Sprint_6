import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from data import OrderData, OrderSuccessText
from locators.order_page_locators import OrderPageLocator

class OrderPageScooter:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    @allure.step('Ввод имени')
    def set_name(self, data_source):
        name_field = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.name_input))
        data = getattr(OrderData, data_source)
        name_field.send_keys(data["name"])   

    @allure.step('Ввод фамилии')
    def set_surname(self, data_source):
        surname_field = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.surname_input))
        data = getattr(OrderData, data_source)
        surname_field.send_keys(data["surname"])

    @allure.step('Ввод адреса')
    def set_address(self, data_source):
        address_field = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.address_input))
        data = getattr(OrderData, data_source)
        address_field.send_keys(data["address"])

    @allure.step('Ввод станции метро')
    def set_subway_station(self):
        self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.subway_station_select)).click()
        subway_station = self.wait.until(expected_conditions.visibility_of_element_located(OrderPageLocator.subway_station_example))
        subway_station.click()   

    @allure.step('Ввод телефона')
    def set_phone(self, data_source):
        phone_field = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.phone_input))
        data = getattr(OrderData, data_source)
        phone_field.send_keys(data["phone"])

    @allure.step('Переход на следующую страницу')
    def click_next_step_button(self):
        button = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.next_step_button))           
        button.click()       

    @allure.step('Ввод даты доставки')
    def set_delivery_date(self, data_source):
        deliver_date = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.delivery_date))
        data = getattr(OrderData, data_source)
        deliver_date.send_keys(data["delivery_date"])
        deliver_date.send_keys(Keys.ENTER)      

    @allure.step('Ввод времени аренды')
    def set_rent_time(self):   
        rent_time_select = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.rent_time_select))
        rent_time_select.click()
        rent_time = self.wait.until(expected_conditions.visibility_of_element_located(OrderPageLocator.rent_time_example))
        rent_time.click() 

    @allure.step('Выбор цвета')
    def set_color_1(self):
        color_pickup_button = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.black_color_checkbox))
        color_pickup_button.click()

    @allure.step('Выбор цвета')
    def set_color_2(self):
        color_pickup_button = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.grey_color_checkbox))
        color_pickup_button.click()

    @allure.step('Сообщение для курьера')
    def set_comm_for_courier(self, data_source):
        comm_for_courier = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.comm_for_courier))
        data = getattr(OrderData, data_source)
        comm_for_courier.send_keys(data["message"])        

    @allure.step('Подтверждение заказа')
    def click_confirm_order_button(self):
        button = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.confirm_order_button))           
        button.click()     

    @allure.step('Проверка статуса')
    def click_status_check_button(self):
        status_check_button = self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocator.status_check_button))           
        status_check_button.click()   

    @allure.step('Проверка успешного заказа')
    def order_success_message(self):
        order_success_message = self.wait.until(expected_conditions.visibility_of_element_located(OrderPageLocator.order_success_header))
        return order_success_message

    @allure.title('Проверка формы заказа с набором данных')
    def check_order_form(self, data_source):
        self.set_name(data_source)
        self.set_surname(data_source)
        self.set_address(data_source)
        self.set_subway_station()
        self.set_phone(data_source)
        self.click_next_step_button()
        self.set_delivery_date(data_source)
        self.set_rent_time()
        self.set_color_1()
        self.set_comm_for_courier(data_source)
        self.click_next_step_button()
        self.click_confirm_order_button()
