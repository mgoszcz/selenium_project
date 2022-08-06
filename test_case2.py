from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from my_selectors import CssSelector

driver = webdriver.Chrome()

accept_cookies_button_css_selector = CssSelector('button', 'id', 'L2AGLb')
search_box_css_selector = CssSelector('input', 'class', 'gLFyf gsfi')
search_button_css_selector = CssSelector('input', 'class' ,'gNO89b')
search_result_css_selector = CssSelector('a', 'href', 'https://www.lambdatest.com/')


driver.get('https://www.google.com')

button = driver.find_elements(By.CSS_SELECTOR, accept_cookies_button_css_selector.print())

if button:
    button[0].click()

search_box = driver.find_element(By.CSS_SELECTOR, search_box_css_selector.print())
search_box.send_keys('LambdaTest')
search_box.submit()

search_results = driver.find_elements(By.CSS_SELECTOR, search_result_css_selector.print())

assert len(search_results) > 0

search_results[0].click()
current_url = driver.current_url

assert "https://www.lambdatest.com/" in current_url
driver.close()
