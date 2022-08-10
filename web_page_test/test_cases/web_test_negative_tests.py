"""Contains NegativeTests class"""
from web_page_test.shared.web_test_base_test_class import WebTestBaseTestClass
from web_page_test.shared.web_test_test_data import WebTestTestData


class WebTestNegativeTests(WebTestBaseTestClass):
    """Class holds all negative test cases"""
    def _negative_scenario_verifier(self):
        """
        Common verifier for negative scenarios
        Veirfy displayed message, log in button still available and input fields are cleared
        """
        self._verify_message(expected_message=WebTestTestData.login_fail_message,
                             assert_message='Verify message after log in failed')
        self.assertEqual('Log In', self.button_object.text, msg='Verify Log In button available')
        self._verify_text_inputs()

    def test_negative_both_fields_empty(self):
        """Verify log in fails when both fields are empty"""
        self.button_object.click()
        self._negative_scenario_verifier()

    def test_negative_empty_user(self):
        """Verify log in fails when user name is empty and password is correct"""
        self._login_user('', WebTestTestData.correct_password)
        self._negative_scenario_verifier()

    def test_negative_empty_password(self):
        """Verify log in fails when user name is correct and password is empty"""
        self._login_user(WebTestTestData.user_names[0], '')
        self._negative_scenario_verifier()

    def test_negative_wrong_password(self):
        """Verify log in fails when user name is correct and password is wrong"""
        self._login_user(WebTestTestData.user_names[0], WebTestTestData.invalid_password)
        self._negative_scenario_verifier()

    def test_negative_very_long_password(self):
        """Verify log in fails when user name is correct and password is wrong and very long (400 chars)"""
        self._login_user(WebTestTestData.user_names[0], WebTestTestData.long_password)
        self._negative_scenario_verifier()