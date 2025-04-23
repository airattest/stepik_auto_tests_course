import time
import math

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element(("id", "price"), "$100")
    )
driver.find_element("id", "book").click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element("xpath", "//label/span[@id='input_value']")
x = x_element.text
y = calc(x)

input_field = driver.find_element("xpath", "//div/input[@id='answer']")
input_field.send_keys(y)

driver.find_element("xpath", "//button[@type='submit']").click()

time.sleep(5)