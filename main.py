"""https://www.lambdatest.com/blog/getting-started-with-selenium-python/"""
import time
from unittest import TestCase


from selenium import webdriver
from selenium.webdriver.common.by import By

from my_selectors import CssSelector



items_list_css_selector = CssSelector('ul', 'class', 'list-unstyled')
list_item_css_selector = CssSelector('input', 'name', '{}')
form_input_css_selector = CssSelector('input', 'id', 'sampletodotext')
form_add_button = CssSelector('input', 'id', 'addbutton')

class WebTest(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = None


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')

    def tearDown(self) -> None:
        self.driver.close()


    def verify_item_added(self):
        items_list = self.driver.find_element(By.CSS_SELECTOR, items_list_css_selector.print())
        items = items_list.find_elements(By.TAG_NAME, 'li')
        passed = False
        for item in items:
            if item.text == 'Happy Testing at LambdaTest':
                passed = True
        assert passed

    def test_click_first_two_items_2(self):

        items_list = self.driver.find_element(By.CSS_SELECTOR, items_list_css_selector.print())
        items = items_list.find_elements(By.TAG_NAME, 'li')
        for item in items[:2]:
            item.find_element(By.TAG_NAME, 'input').click()
        done_true_elements = self.driver.find_elements(By.CSS_SELECTOR, 'span.done-true')
        assert len(done_true_elements) == 2

    def test_add_new_item(self):
        input_object = self.driver.find_element(By.CSS_SELECTOR, form_input_css_selector.print())
        input_object.send_keys('Happy Testing at LambdaTest')
        add_button = self.driver.find_element(By.CSS_SELECTOR, form_add_button.print())
        add_button.click()
        self.verify_item_added

