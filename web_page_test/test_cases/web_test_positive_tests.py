"""Contains PositiveTests class"""
from web_page_test.shared.web_test_base_test_class import WebTestBaseTestClass
from web_page_test.shared.web_test_test_data import WebTestTestData


class WebTestPositiveTests(WebTestBaseTestClass):
    """Class holds test cases for positive testing"""

    def _logging_user_positive(self, user_name: str, password: str):
        """
        Common method to log user and verify - positive so log in must success
        Verify personalized message, button logo off presence and test inputs contains user name and password
        """
        self._login_user(user_name, password)
        self._verify_message(WebTestTestData.welcome_message.format(user_name),
                             'Verify personalized welcome message is displayed')
        self.assertEqual('Log Out', self.button_object.text, msg='Verify Log Out button available')
        self._verify_text_inputs(user_name, password)

    def test_logging_first_user(self):
        """Verify logging first user"""
        self._logging_user_positive(WebTestTestData.user_names[0], WebTestTestData.correct_password)

    def test_logging_second_user(self):
        """Verify logging second user"""
        self._logging_user_positive(WebTestTestData.user_names[1], WebTestTestData.correct_password)

    def test_logging_third_user(self):
        """Verify logging third user"""
        self._logging_user_positive(WebTestTestData.user_names[2], WebTestTestData.correct_password)

    def test_logging_very_long_user_name(self):
        """Verify logging user with 400 characters long name"""
        self._logging_user_positive(WebTestTestData.long_user_name, WebTestTestData.correct_password)

    def test_logout(self):
        """Verify logoff (need to log in first)"""
        self._login_user(WebTestTestData.user_names[0], WebTestTestData.correct_password)
        self.button_object.click()
        self._verify_message(expected_message=WebTestTestData.logoff_message,
                             assert_message='Verify message after log out')
        self.assertEqual('Log In', self.button_object.text, msg='Verify Log In button available')
        self._verify_text_inputs()
