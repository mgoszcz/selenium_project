"""Module contains BaseTestClass"""
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By

from web_page_test.shared.web_test_selectors import WebTestSelectors


class WebTestBaseTestClass(TestCase):
    """Class holds common procedures used in web testing"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = None
        self.user_input_object = None
        self.password_input_object = None
        self.button_object = None

    def _login_user(self, user: str, user_password: str) -> None:
        """Enter user name and password and click log in button"""
        self.user_input_object.send_keys(user)
        self.password_input_object.send_keys(user_password)
        self.button_object.click()

    def _verify_message(self, expected_message: str, assert_message: str) -> None:
        """Verify message displayed is the same as expected"""
        message = self.driver.find_element(By.CSS_SELECTOR, WebTestSelectors.message_label)
        self.assertEqual(expected_message, message.text, msg=assert_message)

    def _verify_text_inputs(self, expected_user: str = '', expected_password: str = ''):
        """
        Verify text inputs fields
        When no parameters provided it will verify if text inputs are empty
        """
        self.assertEqual(expected_user, self.user_input_object.get_property('value'), 'Verify user name field content')
        self.assertEqual(expected_password, self.password_input_object.get_property('value'),
                         'Verify password field content')

    def setUp(self) -> None:
        """Set up method - start browser, open URL and find commonly used objects"""
        self.driver = webdriver.Chrome()
        self.driver.get('http://uitestingplayground.com/sampleapp')
        self.user_input_object = self.driver.find_element(By.CSS_SELECTOR, WebTestSelectors.user_name_input_selector)
        self.password_input_object = self.driver.find_element(By.CSS_SELECTOR, WebTestSelectors.password_input_selector)
        self.button_object = self.driver.find_element(By.CSS_SELECTOR, WebTestSelectors.login_button)

    def tearDown(self) -> None:
        """Tear down method - close web browser"""
        self.driver.close()
