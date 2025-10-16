from selenium.webdriver.common.by import By


class MainPage:
    LOGIN_REGISTER_BTN = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]") # Главная кнопка в шапке 'Вход и регистрация'
    PUBLISH_BTN = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]") # Кнопка "Разместить объявление"
    AVATAR_BTN = (By.XPATH, "//button[@class='circleSmall']") # Аватар пользователя
    USER_NAME = (By.CLASS_NAME, "profileText") # Имя пользователя
    LOGOUT_BTN = (By.XPATH, "//button[text()='Выйти']") # Кнопка выхода под именем пользователя
    PUBLICATION_ELEMENT = (By.XPATH, "//*[@class='card']") # Карточка объявления

class LogInPopUp:
    HEADER = (By.XPATH, "//h1[text()='Войти']") # Заголовок всплывающего окна входа
    LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка входа во всплывающем окне входа
    NO_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]") # Кнопка об отсутствии аккаунта

class RegisterPopUp:
    HEADER = (By.XPATH, "//h1[text()='Зарегистрироваться']") # Заголовок всплывающего окна регистрации
    PASSWORD_SUBMIT_INPUT = (By.NAME, "submitPassword") # Поле повторного ввода пароля
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]") # Кнопка создания аккаунта
    HAVE_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(), 'Уже есть аккаунт')]") # Кнопка "Уже есть аккаунт"
    HIDE_PASSWORD_BTN = (By.CLASS_NAME, "eyeButton") # Кнопка показать и скрыть пароль
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Ошибка')]")

class CommonElements:
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Введите Email']") # Поле ввода почты
    PASSWORD_INPUT = (By.NAME, "password") # Поле ввода пароля
    CLOSE_BTN = (By.XPATH, "//*[@class='h1']/following-sibling::button") # Кнопка закрытия всплывающего окна
    EMAIL_PARENT_ELEMENT = (By.XPATH, "//input[@placeholder='Введите Email']/parent::div")
    PASSWORD_PARENT_ELEMENT = (By.XPATH, "//input[@placeholder='Пароль']/parent::div")
    SUBMIT_PASSWORD_PARENT_ELEMENT = (By.XPATH, "//input[@placeholder='Повторите пароль']/parent::div")
    POPUP_HEADER = (By.XPATH, "//h1")

class PublicationForm:
    TITLE = (By.XPATH, "//input[@placeholder='Название']") # Название
    DESCRIPTION = (By.XPATH, "//*[@placeholder='Описание товара']") # Описание
    PRICE = (By.XPATH, "//*[@placeholder='Стоимость']") # Стоимость
    DROPDOWN = [
        (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[1]/button"),
        (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[3]/div[1]/button")
    ] # Выпадающий список
    PUBLISH_BTN = (By.XPATH, "//button[@type='submit']") # Кнопка публикации

def radio_choose(driver, value):
    return driver.find_element(By.XPATH, f"//*[@value='{value}']")

def type_choose(driver, parameter):
    return driver.find_element(By.XPATH, f"//*[contains(text(), '{parameter}')]")