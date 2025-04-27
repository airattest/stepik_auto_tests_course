import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://suninjuly.github.io/huge_form.html")

elements = driver.find_elements("xpath", "//div/input")
print(len(elements))
for i in elements:
    i.send_keys("Мой ответ")

time.sleep(3)
button = driver.find_element("css selector", "button.btn")
button.click()
time.sleep(10)