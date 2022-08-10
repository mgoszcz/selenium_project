"""Module contains Selectors class"""


class WebTestSelectors:
    """Class holds all selectors used in test"""
    user_name_input_selector = 'input.form-control[name=UserName]'
    password_input_selector = 'input.form-control[name=Password]'
    login_button = 'button#login'
    message_label = 'label#loginstatus'
