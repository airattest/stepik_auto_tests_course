import math
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver.get("https://suninjuly.github.io/get_attribute.html")

x_element = driver.find_element("xpath", "//h2/img[@id='treasure']")
x = x_element.get_attribute("valuex") # Получаем значение атрибута valuex
y = calc(x)

input_field = driver.find_element("xpath", "//input[@id='answer']")
input_field.send_keys(y)

driver.find_element("xpath", "//input[@id='robotsRule']").click()
driver.find_element("xpath", "//input[@id='robotCheckbox']").click()
driver.find_element("xpath", "//button[@type='submit']").click()

time.sleep(10)