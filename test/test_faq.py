import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.home_page import HomePageScooter

class TestFaqList():

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 3)

    def test_FAQ_1_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)

        HomePage.scroll_to_faq()
        self.wait.until(expected_conditions.visibility_of_element_located(HomePage.FAQ_window))

        HomePage.click_FAQ_1()
        FAQ_1 = self.driver.find_element(*HomePage.FAQ_1_text).text
        assert FAQ_1 == HomePage.correct_FAQ_1_text

    def test_FAQ_2_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)

        HomePage.scroll_to_faq()
        self.wait.until(expected_conditions.visibility_of_element_located(HomePage.FAQ_window))

        HomePage.click_FAQ_2()
        FAQ_2 = self.driver.find_element(*HomePage.FAQ_2_text).text
        assert FAQ_2 == HomePage.correct_FAQ_2_text

    def test_FAQ_3_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)

        HomePage.scroll_to_faq()
        self.wait.until(expected_conditions.visibility_of_element_located(HomePage.FAQ_window))

        HomePage.click_FAQ_3()
        FAQ_3 = self.driver.find_element(*HomePage.FAQ_3_text).text
        assert FAQ_3 == HomePage.correct_FAQ_3_text
        
    def test_FAQ_4_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)

        HomePage.scroll_to_faq()
        self.wait.until(expected_conditions.visibility_of_element_located(HomePage.FAQ_window))

        HomePage.click_FAQ_4()
        FAQ_4 = self.driver.find_element(*HomePage.FAQ_4_text).text
        assert FAQ_4 == HomePage.correct_FAQ_4_text  

    def test_FAQ_5_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)

        HomePage.scroll_to_faq()
        self.wait.until(expected_conditions.visibility_of_element_located(HomePage.FAQ_window))

        HomePage.click_FAQ_5()
        FAQ_5 = self.driver.find_element(*HomePage.FAQ_5_text).text
        assert FAQ_5 == HomePage.correct_FAQ_5_text
        
    def test_FAQ_6_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)

        HomePage.scroll_to_faq()
        self.wait.until(expected_conditions.visibility_of_element_located(HomePage.FAQ_window))

        HomePage.click_FAQ_6()
        FAQ_6 = self.driver.find_element(*HomePage.FAQ_6_text).text
        assert FAQ_6 == HomePage.correct_FAQ_6_text 

    def test_FAQ_7_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)

        HomePage.scroll_to_faq()
        self.wait.until(expected_conditions.visibility_of_element_located(HomePage.FAQ_window))

        HomePage.click_FAQ_7()
        FAQ_7 = self.driver.find_element(*HomePage.FAQ_7_text).text
        assert FAQ_7 == HomePage.correct_FAQ_7_text
        
    def test_FAQ_8_correct_text(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        HomePage = HomePageScooter(self.driver)

        HomePage.scroll_to_faq()
        self.wait.until(expected_conditions.visibility_of_element_located(HomePage.FAQ_window))

        HomePage.click_FAQ_8()
        FAQ_8 = self.driver.find_element(*HomePage.FAQ_8_text).text
        assert FAQ_8 == HomePage.correct_FAQ_8_text         

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    