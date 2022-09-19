import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser=webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys('german')
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys('german')
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys('german')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt.docx')
    browser.find_element(By.CSS_SELECTOR, "[name='file']").send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)