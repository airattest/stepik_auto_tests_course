import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://SunInJuly.github.io/execute_script.html")
button = driver.find_element("tag name", "button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(5)

driver.execute_script("window.scrollBy(0, 100);") # скролл страницы
# button = document.getElementsByTagName("button")[0]; # тоже самое только на JS
# button.scrollIntoView(true);

# driver.execute_script("document.title='Script executing';alert('Robots at work');") # вызов алерта
