from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)

driver.get("http://suninjuly.github.io/wait1.html")

button = driver.find_element("id", "verify")
button.click()
message = driver.find_element("id", "verify_message")

assert "successful" in message.text
