"""https://www.lambdatest.com/blog/getting-started-with-selenium-python/"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

items_list_css_selector = "ul[class=list-unstyled]"
css_selector = 'input[name={}]'
xpath_selector = "//input[@name='{}']"
form_input_css_selector = "input[id=sampletodotext]"
form_add_button = "input[id=addbutton]"

def click_first_two_items_1():
    # driver.find_element(By.NAME, 'li1').click()
    driver.find_element(By.CSS_SELECTOR, css_selector.format('li1')).click()
    # driver.find_element(By.XPATH, xpath_selector.format('li1')).click()
    driver.find_element(By.CSS_SELECTOR, css_selector.format('li2')).click()
    # driver.find_element(By.XPATH, xpath_selector.format('li2')).click()

def click_first_two_items_2():
    items_list = driver.find_element(By.CSS_SELECTOR, items_list_css_selector)
    items = items_list.find_elements(By.TAG_NAME, 'li')
    for item in items[:2]:
        item.find_element(By.TAG_NAME, 'input').click()

def add_new_item():
    input = driver.find_element(By.CSS_SELECTOR, form_input_css_selector)
    input.send_keys('Happy Testing at LambdaTest')
    add_button = driver.find_element(By.CSS_SELECTOR, form_add_button)
    add_button.click()

def verify_item_added():
    items_list = driver.find_element(By.CSS_SELECTOR, items_list_css_selector)
    items = items_list.find_elements(By.TAG_NAME, 'li')
    passed = False
    for item in items:
        if item.text == 'Happy Testing at LambdaTest':
            passed = True
    assert passed

driver.get('https://lambdatest.github.io/sample-todo-app/')
# click_first_two_items_1()
click_first_two_items_2()
add_new_item()
verify_item_added()
pass