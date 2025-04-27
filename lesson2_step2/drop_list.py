import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import Select

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://suninjuly.github.io/selects1.html?")

element_num_1 = driver.find_element("xpath", "//h2/span[@id='num1']")
num_1 = element_num_1.text
element_num_2 = driver.find_element("xpath", "//h2/span[@id='num2']")
num_2 = element_num_2.text
num_summ = str(int(num_1) + int(num_2))
print(num_summ)

select = Select(driver.find_element("tag name", "select")) # находим список со значениями select
select.select_by_value(num_summ) # выбрать по значению

driver.find_element("xpath", "//button").click()

time.sleep(10)
