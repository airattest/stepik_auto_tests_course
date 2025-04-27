import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

link = "https://suninjuly.github.io/registration1.html"
driver.get(link)

first_name_input = driver.find_element("xpath", "//input[@placeholder='Input your first name']")
first_name_input.send_keys("Вася")
last_name_input = driver.find_element("xpath", "//input[@placeholder='Input your last name']")
last_name_input.send_keys("Мамонов")
email_input = driver.find_element("xpath", "//input[@placeholder='Input your email']")
email_input.send_keys("mamonshmamon@mail.ru")

# Отправляем заполненную форму
button = driver.find_element("css selector", "button.btn")
button.click()
# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)
# находим элемент, содержащий текст
welcome_text_elt = driver.find_element("tag name", "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text, "Ошибка регистрации"
