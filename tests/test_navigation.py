from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from curl import *


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login):
        """ Проверь переход по клику на «Личный кабинет». """
        driver = login

        driver.find_element(*MainPageLocators.PERSONAL_CABINET).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Lk.INFO_MESSAGE))
        profile = driver.find_element(*Lk.SHOP_BUTTON)
        assert url_profile == driver.current_url and profile.text == 'История заказов'

    def test_click_constructor_button_show_constructor_form(self, login):
        """ Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers. """
        driver = login

        driver.find_element(*MainPageLocators.PERSONAL_CABINET).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Lk.INFO_MESSAGE))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logo_button_show_constructor_form(self, login):
        """ Переход из личного кабинета в конструктор при нажатии на лого """
        driver = login

        driver.find_element(*MainPageLocators.PERSONAL_CABINET).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Lk.INFO_MESSAGE))
        driver.find_element(*MainPageLocators.LOGO).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logout_button_in_lk_open_login_form(self, login):
        """ Проверь выход по кнопке «Выйти» в личном кабинете. """
        driver = login

        driver.find_element(*MainPageLocators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(Lk.INFO_MESSAGE))

        driver.find_element(*Lk.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TEXT))

        login_button = driver.find_element(*LoginPageLocators.LOGIN_TEXT)
        assert driver.current_url == url_login and login_button.text == 'Вход'
