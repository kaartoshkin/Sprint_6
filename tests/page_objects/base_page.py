from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePageScooter:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"
        self.wait = WebDriverWait(driver, 3)

    def open(self):
        self.driver.get(self.base_url)
