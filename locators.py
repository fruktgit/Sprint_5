from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    PERSONAL_CABINET = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Ссылка "Личный кабинет"
    MAIN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    MAIN_LOGIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    SAUCE_BUTTON = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    SAUCE= By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"

    TOPPINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    TOPPINGS = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"

    BUN_BUTTON = (By.XPATH, ".//span[text()='Булки']/parent::*")
    BUN = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"

class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")  # Поле "Имя"
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")  # Поле "Email"
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")  # Поле "Пароль"
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    ERROR_TEXT = (By.XPATH, ".//p[contains(@class, 'input__error')]")


class ConstructorLocators:
    BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]')  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]')  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]')  # Раздел "Начинки"

class LoginPageLocators:
    LOGIN_TEXT = (By.XPATH, ".//*[text() = 'Вход']")  # текст Вход
    LOGIN_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON= (By.XPATH, ".//button[text()='Войти']")
    LOGIN_ENTER = (By.XPATH, ".//a[text()='Войти']")


class AuthPassword:
    LOGIN_PASS_FORGOT = (By.XPATH, ".//a[text()='Войти']")

class Lk:
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    INFO_MESSAGE = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
    SHOP_BUTTON = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")