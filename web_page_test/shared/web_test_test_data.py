"""Module contains TestData class"""


class WebTestTestData:
    """Class holds all test data used in test"""
    user_names = ['user', 'any', 'marcin']
    correct_password = 'pwd'
    welcome_message = 'Welcome, {}!'
    logoff_message = 'User logged out.'
    login_fail_message = 'Invalid username/password'
    invalid_password = 'invalid'
    long_user_name = 'user' * 100
    long_password = 'pass' * 100
