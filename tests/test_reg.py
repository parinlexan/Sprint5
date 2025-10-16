import random
import string

from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

import data
from locators import MainPage, LogInPopUp, RegisterPopUp, CommonElements

incorrect_email = ''.join(random.choices(string.ascii_lowercase, k=10))


class TestRegistration:

    def test_registration(self, driver, register, generate_random_email, generate_random_password):
        # Открываем бразуер и переходим на нужный сайт
        driver.get(data.URL)
        # Нажимаем на кнопку "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_REGISTER_BTN).click()
        # Ожидаем появление всплывающего окна
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(LogInPopUp.NO_ACCOUNT_BTN)
        )

        # Кликаем по кнопку "Нет аккаунта"
        driver.find_element(*LogInPopUp.NO_ACCOUNT_BTN).click()

        # Ожидаем перехода в раздел регистрации
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(RegisterPopUp.HEADER)
        )

        # Вводим почту
        driver.find_element(*CommonElements.EMAIL_INPUT).send_keys(generate_random_email)

        # Вводим пароль
        driver.find_element(*CommonElements.PASSWORD_INPUT).send_keys(generate_random_password)

        # Подтверждаем пароль
        driver.find_element(*RegisterPopUp.PASSWORD_SUBMIT_INPUT).send_keys(generate_random_password)

        # Нажимаем кнопку создания аккаунта
        driver.find_element(*RegisterPopUp.CREATE_ACCOUNT_BTN).click()

        # Проверяем появление аватара
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(MainPage.AVATAR_BTN)
        )

        # Проверяем появление имени пользователя
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(MainPage.USER_NAME)
        )

    def test_wrong_email_registration(self, driver):
        # Открываем бразуер и переходим на нужный сайт
        driver.get(data.URL)
        # Нажимаем на кнопку "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_REGISTER_BTN).click()
        # Ожидаем появление всплывающего окна
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(LogInPopUp.NO_ACCOUNT_BTN)
        )

        # Кликаем по кнопку "Нет аккаунта"
        driver.find_element(*LogInPopUp.NO_ACCOUNT_BTN).click()

        # Ожидаем перехода в раздел регистрации
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(RegisterPopUp.HEADER)
        )

        # Вводим неверную почту
        driver.find_element(*CommonElements.EMAIL_INPUT).send_keys(incorrect_email)

        # Нажимаем кнопку создания аккаунта
        driver.find_element(*RegisterPopUp.CREATE_ACCOUNT_BTN).click()

        # Проверяем появление текста ошибки
        assert WebDriverWait(driver, 10).until(
            visibility_of_element_located(RegisterPopUp.ERROR_MESSAGE)
        ).is_displayed()

        # Проверяем покраснение поля почты
        assert '_inputError_' in driver.find_element(*CommonElements.EMAIL_PARENT_ELEMENT).get_attribute('class')

        # Проверяем покраснение полей для ввода пароля
        assert '_inputError_' in driver.find_element(*CommonElements.PASSWORD_PARENT_ELEMENT).get_attribute('class')
        assert '_inputError_' in driver.find_element(*CommonElements.SUBMIT_PASSWORD_PARENT_ELEMENT).get_attribute(
            'class')

    def test_existing_user_register(self, driver, generate_random_email, generate_random_password):
        # Открываем бразуер и переходим на нужный сайт
        driver.get(data.URL)
        # Нажимаем на кнопку "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_REGISTER_BTN).click()
        # Ожидаем появление всплывающего окна
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(LogInPopUp.NO_ACCOUNT_BTN)
        )

        # Кликаем по кнопку "Нет аккаунта"
        driver.find_element(*LogInPopUp.NO_ACCOUNT_BTN).click()

        # Ожидаем перехода в раздел регистрации
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(RegisterPopUp.HEADER)
        )

        # Вводим почту
        driver.find_element(*CommonElements.EMAIL_INPUT).send_keys(generate_random_email)

        # Вводим пароль
        driver.find_element(*CommonElements.PASSWORD_INPUT).send_keys(generate_random_password)

        # Подтверждаем пароль
        driver.find_element(*RegisterPopUp.PASSWORD_SUBMIT_INPUT).send_keys(generate_random_password)

        # Нажимаем кнопку создания аккаунта
        driver.find_element(*RegisterPopUp.CREATE_ACCOUNT_BTN).click()

        # Проверяем появление аватара
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(MainPage.AVATAR_BTN)
        )

        # Выходим из аккаунта
        driver.find_element(*MainPage.LOGOUT_BTN).click()

        # Ожидаем появление кнопки "Вход и регистрация"
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(MainPage.LOGIN_REGISTER_BTN)
        )

        # Нажимаем на кнопку "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_REGISTER_BTN).click()

        # Ожидаем появление всплывающего окна
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(LogInPopUp.NO_ACCOUNT_BTN)
        )

        # Кликаем по кнопку "Нет аккаунта"
        driver.find_element(*LogInPopUp.NO_ACCOUNT_BTN).click()

        # Ожидаем перехода в раздел регистрации
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(RegisterPopUp.HEADER)
        )

        # Вводим почту
        driver.find_element(*CommonElements.EMAIL_INPUT).send_keys(generate_random_email)

        # Вводим пароль
        driver.find_element(*CommonElements.PASSWORD_INPUT).send_keys(generate_random_password)

        # Подтверждаем пароль
        driver.find_element(*RegisterPopUp.PASSWORD_SUBMIT_INPUT).send_keys(generate_random_password)

        # Нажимаем кнопку создания аккаунта
        driver.find_element(*RegisterPopUp.CREATE_ACCOUNT_BTN).click()

        # Проверяем появление текста ошибки
        assert WebDriverWait(driver, 10).until(
            visibility_of_element_located(RegisterPopUp.ERROR_MESSAGE)
        ).is_displayed()

        # Проверяем покраснение поля почты
        assert '_inputError_' in driver.find_element(*CommonElements.EMAIL_PARENT_ELEMENT).get_attribute('class')

        # Проверяем покраснение полей для ввода пароля
        assert '_inputError_' in driver.find_element(*CommonElements.PASSWORD_PARENT_ELEMENT).get_attribute('class')
        assert '_inputError_' in driver.find_element(*CommonElements.SUBMIT_PASSWORD_PARENT_ELEMENT).get_attribute(
            'class')
