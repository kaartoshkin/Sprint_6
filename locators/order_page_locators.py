import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from data import OrderData, OrderSuccessText

class OrderPageLocator:
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