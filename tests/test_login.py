import pytest

import generators
from locators import *
from generators import *
from curl import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Login:

    def test_login_main_page(self, driver):
        #вход по кнопке «Войти в аккаунт» на главной

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TEXT))

        driver.find_element(*LoginPageLocators.LOGIN_EMAIL_FIELD).send_keys(PersonData.login)
        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD).send_keys(PersonData.password)

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPageLocators.MAIN_ORDER_BUTTON))

        order_button = driver.find_element(*MainPageLocators.MAIN_ORDER_BUTTON)
        assert driver.current_url == main_site

    def test_login_main_login_button(self, driver):
        #вход через кнопку «Личный кабинет»

        driver.find_element(*MainPageLocators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TEXT))

        driver.find_element(*LoginPageLocators.LOGIN_EMAIL_FIELD).send_keys(PersonData.login)
        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD).send_keys(PersonData.password)

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPageLocators.MAIN_ORDER_BUTTON))

        order_button = driver.find_element(*MainPageLocators.MAIN_ORDER_BUTTON)
        assert driver.current_url == main_site

    def test_login_button_registration(self, driver):
        # вход через кнопку в форме регистрации
        driver.get(url_register)

        driver.find_element(*LoginPageLocators.LOGIN_ENTER).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TEXT))

        driver.find_element(*LoginPageLocators.LOGIN_EMAIL_FIELD).send_keys(PersonData.login)
        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD).send_keys(PersonData.password)

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPageLocators.MAIN_ORDER_BUTTON))

        order_button = driver.find_element(*MainPageLocators.MAIN_ORDER_BUTTON)
        assert driver.current_url == main_site

    def test_login_button_registration(self, driver):
        # вход через кнопку в форме восстановления пароля

        driver.get(url_forgot_password)

        driver.find_element(*AuthPassword.LOGIN_PASS_FORGOT).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TEXT))

        driver.find_element(*LoginPageLocators.LOGIN_EMAIL_FIELD).send_keys(PersonData.login)
        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD).send_keys(PersonData.password)

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPageLocators.MAIN_ORDER_BUTTON))

        order_button = driver.find_element(*MainPageLocators.MAIN_ORDER_BUTTON)
        assert driver.current_url == main_site