import math
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    ans = alert.text.split()[-1]
    print(ans)
    alert.accept()

    return ans


def stepik_auth(remote: webdriver.Remote):
    remote.get(auth_link)
    WebDriverWait(remote, 3).until(lambda x: x.find_element_by_name("login"))
    auth_elems = ("login", "password")

    for auth_elem in auth_elems:
        remote.find_element_by_name(auth_elem).send_keys(os.getenv(auth_elem))
    remote.find_element_by_class_name("sign-form__btn").click()
    WebDriverWait(
        remote,
        3).until(lambda x: x.find_element_by_class_name("navbar__profile-img"))


def stepik_send_answer(remote: webdriver.Remote, answer: str):
    remote.get("https://stepik.org/lesson/184253/step/4?unit=158843")
    WebDriverWait(remote,
                  3).until(lambda x: x.find_element_by_tag_name("textarea"))
    remote.find_element_by_tag_name("textarea").send_keys(answer)
    remote.find_element_by_class_name("submit-submission").click()
    WebDriverWait(remote, 3).until(lambda x: x.find_element_by_id("correct"))


link = "http://suninjuly.github.io/alert_accept.html"
auth_link = "https://stepik.org/catalog?auth=login"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
    browser.switch_to.alert.accept()
    WebDriverWait(browser,
                  5).until(lambda x: x.find_element_by_id("input_value"))
    browser.find_element_by_id("answer").send_keys(
        calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
    answer = print_answer(browser)
    stepik_auth(browser)
    stepik_send_answer(browser, answer)
finally:
    browser.quit()
С
отправкой
ответа
на
Stepik.

Верное
решение  # 119081855
28.9122825109404
11

User
avatar
Anonymous
173781481
3
года
назад
Подключила
библиотеку: pip
install
pyperclip

Потом
запустила
файл, который
полностью, автоматизировано, получает
ответ, переходит
на
страницу
данного
шага
и
отправляет
ответ.

from selenium import webdriver
import time
import math
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn").click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    # Считать значение для переменной x
    x = browser.find_element_by_id("input_value").text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    browser.find_element_by_id("answer").send_keys(y)

    # Нажать на кнопку Submit.
    browser.find_element_by_css_selector("button.btn").click()

    # Копируем результат. Спасибо за данный фрагмент кода Vitaliy Ya! =)
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

    # Нажимаем на кноку "Ok"
    alert.accept()

    # Переходим на главную страницу, авторизуемся, затем на страницу с заданием

    browser.get("https://stepik.org/catalog")
    time.sleep(5)
    browser.find_element_by_id("ember32").click()

    s_username = browser.find_element_by_id("id_login_email")
    s_username.send_keys("почта")

    s_password = browser.find_element_by_id("id_login_password")
    s_password.send_keys("пароль")

    # Ищем кнопку для авторизации
    browser.find_element_by_css_selector(".sign-form__btn").click()
    time.sleep(4)

    browser.get("https://stepik.org/lesson/184253/step/4")
    time.sleep(5)

    # Находим поле для ввода ответа
    textarea = browser.find_element_by_css_selector(".textarea")

    # Скролл до текстового поля, иначе элемент не находится
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)

    # Напишем текст ответа в найденное поле
    textarea.send_keys(addToClipBoard)

    # Отправляем ответ
    browser.find_element_by_css_selector(".submit-submission").click()

    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()