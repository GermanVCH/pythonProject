from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
name = r'C:\\Users\\PaoL\\AppData\\Local\\Google\\Chrome\\User Data'
try:
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=" +name)
    browser = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe", options=options)
    browser.get("https://web.telegram.org/z/#458885740")

    browser.find_element(By.CSS_SELECTOR, "[title='Choose emoji, sticker or GIF'").click()
    WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Stickers'")))
    browser.find_element(By.CSS_SELECTOR, "[title='Stickers']").click()
    WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-sticker-id='1443843450869312'")))
    browser.find_element(By.CSS_SELECTOR, "[data-sticker-id='1443843450869312'").click()
    time.sleep(3)
    browser.find_element_by_class_name('Button.send.default.secondary.round.click-allowed').click()

finally:
    time.sleep(30)