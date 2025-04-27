import time
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#driver.get("http://suninjuly.github.io/simple_form_find_task.html")

driver.get("https://suninjuly.github.io/find_link_text")
text = str(math.ceil(math.pow(math.pi, math.e)*10000))
driver.find_element("link text", text).click()

input_first_name = driver.find_element("xpath", "//input[@name='first_name']")
input_first_name.send_keys("Ivan")
input_last_name = driver.find_element("xpath", "//input[@name='last_name']")
input_last_name.send_keys("Petrov")
input_city = driver.find_element("xpath", "(//input[@name='firstname'])[1]")
input_city.send_keys("Smolensk")
input_country = driver.find_element("xpath", "(//input[@name='firstname'])[2]")
input_country.send_keys("Russia")
button = driver.find_element("css selector", "button.btn")
button.click()

time.sleep(10)