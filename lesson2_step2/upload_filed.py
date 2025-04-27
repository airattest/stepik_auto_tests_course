import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://suninjuly.github.io/file_input.html")

driver.find_element("xpath", "//input[@name='firstname']").send_keys("Ivan")
driver.find_element("xpath", "//input[@name='lastname']").send_keys("Ivanov")
driver.find_element("xpath", "//input[@name='email']").send_keys("email")

upload_field = driver.find_element("xpath", "//input[@type='file']")
upload_field.send_keys(f"{os.getcwd()}/lesson2_step2/upload_test.txt")

driver.find_element("xpath", "//button").click()

time.sleep(5)