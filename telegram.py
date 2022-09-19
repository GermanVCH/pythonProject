from selenium import webdriver
import time
name = r'C:\\Users\\PaoL\\AppData\\Local\\Google\\Chrome\\User Data'
try:
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=" +name)
    browser = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe", options=options)
    browser.get("https://web.telegram.org/z/#458885740")
    browser.fin_element_by_class_name('Button.default.translucent.round').click
    browser.find_element_by_id('editable-message-text').send_keys("I love u")
    time.sleep(3)
    browser.find_element_by_class_name('Button.send.default.secondary.round.click-allowed').click()

finally:
    time.sleep(30)