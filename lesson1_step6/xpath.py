import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://suninjuly.github.io/find_xpath_form")

input_first_name = driver.find_element("xpath", "//input[@name='first_name']")
input_first_name.send_keys("Ivan")
input_last_name = driver.find_element("xpath", "//input[@name='last_name']")
input_last_name.send_keys("Petrov")
input_city = driver.find_element("xpath", "(//input[@name='firstname'])[1]")
input_city.send_keys("Smolensk")
input_country = driver.find_element("xpath", "(//input[@name='firstname'])[2]")
input_country.send_keys("Russia")

submit_button = driver.find_element("xpath", "//button[@type='submit']")
submit_button.click()

time.sleep(10)