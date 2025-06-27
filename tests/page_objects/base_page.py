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

    def wait_and_click(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    def wait_for_load(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def scroll_to(self, scroll):
        self.driver.execute_script(scroll)

    def url_wait_to_change(self, url):
        self.wait.until(expected_conditions.url_changes(url))

    def find_element_on_page(self, element):
        return self.driver.find_element(*element)
    
    def get_current_url(self):
        return self.driver.current_url
