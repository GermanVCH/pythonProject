from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    num1x = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    num2x = num2.text
    x = int(num1x) + int(num2x)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))

    time.sleep(2)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
