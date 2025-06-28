import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.home_page import HomePageScooter
from page_objects.base_page import BasePageScooter
from data import FaqText

class TestFaqList:

    @pytest.mark.parametrize(
        "faq_number, expected_text",
        [
            (1, FaqText.correct_FAQ_1_text),
            (2, FaqText.correct_FAQ_2_text),
            (3, FaqText.correct_FAQ_3_text),
            (4, FaqText.correct_FAQ_4_text),
            (5, FaqText.correct_FAQ_5_text),
            (6, FaqText.correct_FAQ_6_text),
            (7, FaqText.correct_FAQ_7_text),
            (8, FaqText.correct_FAQ_8_text)
        ]
    )
    def test_faq_correct_text(self, faq_number, expected_text):

        self.home_page.click_FAQ(faq_number)
        self.home_page.wait_for_load_FAQ(faq_number)
        actual_text = self.home_page.check_FAQ(faq_number)

        assert actual_text == expected_text
