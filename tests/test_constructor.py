from locators import *


class TestStellarBurgersConstructorForm:

    def test_constructor_section_sauces_scroll(self, login):
        """Проверка перехода на "Соусы" """
        driver = login

        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPageLocators.SAUCE_BUTTON).click()

        h_sauce = driver.find_element(*MainPageLocators.SAUCE)

        assert h_sauce.text == 'Соусы'

    def test_constructor_section_filling_scroll (self, login):
        """Проверка перехода на "Начинки" """
        driver = login

        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPageLocators.TOPPINGS_BUTTON).click()
        h_filling = driver.find_element(*MainPageLocators.TOPPINGS)

        assert h_filling.text == 'Начинки'

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        """Проверка перехода на "Булки" """
        driver = login

        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPageLocators.TOPPINGS_BUTTON).click()
        driver.find_element(*MainPageLocators.BUN_BUTTON).click()

        h_ban = driver.find_element(*MainPageLocators.BUN)

        assert h_ban.text == 'Булки'
