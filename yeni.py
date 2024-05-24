import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def notifier(func):
    def wrapper(driver, *args, **kwargs):
        print("Test işləyir:", func.__name__)
        result = func(driver, *args, **kwargs)
        print("Test bitdi:", func.__name__)
        return result
    return wrapper

@pytest.fixture()
def driver():
    # Define your WebDriver initialization code here
    # Example:
    service = Service('path/to/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture()
def element(driver):
    eleCookiesDiv = driver.find_element(By.CSS_SELECTOR, 'div.cookies')
    return eleCookiesDiv

@notifier
def test_color(element):
    assert element.value_of_css_property("background-color") == "rgba(255, 0, 0, 1)", "Test 1 fail"
    
@notifier
def test_height(element):
    assert element.value_of_css_property("height") == "155.2px","Test 2 fail"
