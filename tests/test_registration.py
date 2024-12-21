import pytest
from locators import *
from generators import generate_email, generate_password, generate_password_wrong
from curl import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:

    def test_successful_registration(self, driver): #Успешная регистрация
        driver.get(url_register)

        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys('Test User')
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email())
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(generate_password())
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TEXT))

        login_button = driver.find_element(*LoginPageLocators.LOGIN_TEXT)
        assert driver.current_url == url_login and login_button.text == 'Вход'

    def test_incorrect_password_error(self, driver): #ошибка не коректного ввода пароля
        driver.get(url_register)

        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys('Test User')
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email())
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(generate_password_wrong())
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 8).until(EC.presence_of_element_located(RegistrationPageLocators.ERROR_TEXT))

        assert driver.find_element(*RegistrationPageLocators.ERROR_TEXT).text == 'Некорректный пароль'

