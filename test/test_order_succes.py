import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from page_objects.home_page import HomePageScooter
from page_objects.order_page import OrderPageScooter

class TestOrderSucces:
    
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 3)

    def test_order_with_upper_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)
        OrderPage = OrderPageScooter(self.driver)
        
        HomePage.click_upper_order_button()
        
        name = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.name_input)
                        )
        name.send_keys(OrderPage.ORDER_DATA_1["name"])

        surname = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.surname_input)
                        )
        surname.send_keys(OrderPage.ORDER_DATA_1["surname"])

        address = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.address_input)
                        ) 
        address.send_keys(OrderPage.ORDER_DATA_1["address"])  
             
        self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.subway_station_select)
                        ).click()
        subway_station = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderPage.subway_station_example))
        subway_station.click()        

        phone = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.phone_input)
                        )
        phone.send_keys(OrderPage.ORDER_DATA_1["phone"])

        button = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.next_step_button))           
        button.click()

        deliver_date = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.delivery_date)
                        )
        deliver_date.send_keys(OrderPage.ORDER_DATA_1["delivery_date"])  
        deliver_date.send_keys(Keys.ENTER)      

        rent_time_select = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.rent_time_select)
                        )
        rent_time_select.click()
        rent_time = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderPage.rent_time_example))
        rent_time.click() 

        color_pickup_button = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.black_color_checkbox)
                        )
        color_pickup_button.click()     

        comm_for_courier = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.comm_for_courier)
                        )
        comm_for_courier.send_keys(OrderPage.ORDER_DATA_1["message"])   

        confirm_button = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.next_step_button))           
        confirm_button.click()

        button = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.confirm_order_button))           
        button.click()

        order_success_message = self.wait.until(
            expected_conditions.visibility_of_element_located(OrderPage.order_succes_header))
        assert order_success_message.is_displayed()

        status_check_button = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.status_check_button))           
        status_check_button.click()

        HomePage.click_scooter_logo()  
        assert self.driver.current_url == HomePage.base_url 


    def test_order_with_lower_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)
        OrderPage = OrderPageScooter(self.driver)
        
        HomePage.scroll_to_lower_button()
        HomePage.click_lower_order_button()
        
        name = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.name_input)
                        )
        name.send_keys(OrderPage.ORDER_DATA_2["name"])

        surname = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.surname_input)
                        )
        surname.send_keys(OrderPage.ORDER_DATA_2["surname"])

        address = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.address_input)
                        ) 
        address.send_keys(OrderPage.ORDER_DATA_2["address"])  
             
        self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.subway_station_select)
                        ).click()
        subway_station = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderPage.subway_station_example))
        subway_station.click()        

        phone = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.phone_input)
                        )
        phone.send_keys(OrderPage.ORDER_DATA_2["phone"])

        button = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.next_step_button))           
        button.click()

        deliver_date = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.delivery_date)
                        )
        deliver_date.send_keys(OrderPage.ORDER_DATA_2["delivery_date"])  
        deliver_date.send_keys(Keys.ENTER)      

        rent_time_select = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.rent_time_select)
                        )
        rent_time_select.click()
        rent_time = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderPage.rent_time_example))
        rent_time.click() 

        color_pickup_button = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.grey_color_checkbox)
                        )
        color_pickup_button.click()     

        comm_for_courier = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.comm_for_courier)
                        )
        comm_for_courier.send_keys(OrderPage.ORDER_DATA_2["message"])   

        confirm_button = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.next_step_button))           
        confirm_button.click()

        button = self.wait.until(
            expected_conditions.element_to_be_clickable(OrderPage.confirm_order_button))           
        button.click()

        order_success_message = self.wait.until(
            expected_conditions.visibility_of_element_located(OrderPage.order_succes_header))
        assert order_success_message.is_displayed()    

        HomePage.click_scooter_logo()  
        assert self.driver.current_url == HomePage.base_url 

    def test_logo_redirect(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)
        OrderPage = OrderPageScooter(self.driver)

        HomePage.click_yandex_logo()
        self.wait.until(expected_conditions.url_changes(self.driver.current_url))

        assert 'dzen.ru' in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()