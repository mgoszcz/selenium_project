"""
1. Happy path:
    Use 3 user names and 'pwd' password to log in
        personalized welcome messsage diplayed, log out button avilable, user name and password are still in inputs
    log out
        user logged out message displayed, log in button available, verify inputs are empty (default)
    special characters and a very long string as a user name
2. False tests
    Both fields are empty
        failed to log in message displayed, log in button is available, verify inputs are empty (default)
    Use user name without password
        failed to log in message displayed, log in button is available, verify inputs are empty (default)
    Use password without user name
        failed to log in message displayed, log in button is available, verify inputs are empty (default)
    use user name with wrong password
        special characters and a very long string as a user name
        failed to log in message displayed, log in button is available, verify inputs are empty (default)
3. Security
    SQL injection - try to provide sql command in fields to break database - there is no backend so not need to be done
4. Performance
    1. Loading time (below 400 ms - dependent on requirements)



"""
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By

USER_NAME = 'user'
CORRECT_PASSWORD = 'pwd'
WELCOME_MESSAGE = 'Welcome, {}!'
LOGOFF_MESSAGE = 'User logged out.'
LOGIN_FAIL_MESSAGE = 'Invalid username/password'

# Selectors
user_name_input_selector = 'input.form-control[name=UserName]'
password_input_selector = 'input.form-control[name=Password]'
login_button = 'button#login'
message_label = 'label#loginstatus'


class NewTest(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = None
        self.user_input_object = None
        self.password_input_object = None
        self.button_object = None

    def _login_user(self, user: str, user_password: str) -> None:
        self.user_input_object.send_keys(user)
        self.password_input_object.send_keys(user_password)
        self.button_object.click()

    def _verify_message(self, expected_message: str, assert_message: str) -> None:
        message = self.driver.find_element(By.CSS_SELECTOR, message_label)
        self.assertEqual(expected_message, message.text, msg=assert_message)

    def _verify_text_inputs(self, expected_user: str = '', expected_password: str = ''):
        self.assertEqual(expected_user, self.user_input_object.get_property('value'), 'Verify user name field content')
        self.assertEqual(expected_password, self.password_input_object.get_property('value'),
                         'Verify password field content')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://uitestingplayground.com/sampleapp')
        self.user_input_object = self.driver.find_element(By.CSS_SELECTOR, user_name_input_selector)
        self.password_input_object = self.driver.find_element(By.CSS_SELECTOR, password_input_selector)
        self.button_object = self.driver.find_element(By.CSS_SELECTOR, login_button)

    def tearDown(self) -> None:
        self.driver.close()

    def test_logging_first_user_positive(self):
        self._login_user(USER_NAME, CORRECT_PASSWORD)
        self._verify_message(WELCOME_MESSAGE.format(USER_NAME), 'Verify personalized welcome message is displayed')
        self.assertEqual('Log Out', self.button_object.text, msg='Verify Log Out button available')
        self._verify_text_inputs(USER_NAME, CORRECT_PASSWORD)

    def test_logout(self):
        self._login_user(USER_NAME, CORRECT_PASSWORD)
        self.button_object.click()
        self._verify_message(expected_message=LOGOFF_MESSAGE, assert_message='Verify message after log out')
        self.assertEqual('Log In', self.button_object.text, msg='Verify Log In button available')
        self._verify_text_inputs()

    def test_negative_both_fields_empty(self):
        self.button_object.click()
        self._verify_message(expected_message=LOGIN_FAIL_MESSAGE, assert_message='Verify message after log in failed')
        self.assertEqual('Log In', self.button_object.text, msg='Verify Log In button available')
        self._verify_text_inputs()

    def test_negative_empty_user(self):
        self._login_user('', CORRECT_PASSWORD)
        self._verify_message(expected_message=LOGIN_FAIL_MESSAGE, assert_message='Verify message after log in failed')
        self.assertEqual('Log In', self.button_object.text, msg='Verify Log In button available')
        self._verify_text_inputs()

