import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(30)
    button = browser.find_element("xpath", "(//button[@type='submit'])[2]")
    assert button is not None, "Кнопка добавления в корзину не найдена"
