import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from generators import *
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from curl import *

@pytest.fixture
def driver():
    screen_width, screen_height = pyautogui.size()
    options = Options()
    options.add_argument("--window-size=1400,1050")
    driver = webdriver.Chrome(options=options)
    driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    """ Войти в аккаунт """
    driver.get(url_login)

    driver.find_element(*LoginPageLocators.LOGIN_EMAIL_FIELD).send_keys(PersonData.login)
    driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD).send_keys(PersonData.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(MainPageLocators.MAIN_ORDER_BUTTON))
    return driver


