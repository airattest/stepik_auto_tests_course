import time
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver.get("https://suninjuly.github.io/execute_script.html")

x_element = driver.find_element("xpath", "//label/span[@id='input_value']")
x = x_element.text
y = calc(x)

input_field = driver.find_element("xpath", "//div/input[@id='answer']")
input_field.send_keys(y)
driver.execute_script("window.scrollBy(0, 200);")
driver.find_element("xpath", "//div/input[@id='robotCheckbox']").click()
driver.find_element("xpath", "//div/input[@id='robotsRule']").click()

button = driver.find_element("tag name", "button").click()

time.sleep(5)
