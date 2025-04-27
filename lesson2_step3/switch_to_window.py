import time
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver.get("https://suninjuly.github.io/redirect_accept.html")

first_wondow = driver.window_handles[0] # основная вкладка
driver.find_element("xpath", "//button[@type='submit']").click()
new_window = driver.window_handles[1] # новая открывшаяся вкладка

driver.switch_to.window(new_window) # переключение на нужную вкладку

x_element = driver.find_element("xpath", "//label/span[@id='input_value']")
x = x_element.text
y = calc(x)

input_field = driver.find_element("xpath", "//div/input[@id='answer']")
input_field.send_keys(y)

driver.find_element("xpath", "//button[@type='submit']").click()

time.sleep(5)