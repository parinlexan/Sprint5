from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

import data
from locators import MainPage, LogInPopUp, CommonElements


class TestLogout:

    def test_existing_user_login(self, driver, generate_random_email, generate_random_password):
        # Открываем бразуер и переходим на нужный сайт
        driver.get(data.URL)

        # Нажимаем на кнопку "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_REGISTER_BTN).click()

        # Ожидаем появление всплывающего окна
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(LogInPopUp.NO_ACCOUNT_BTN)
        )

        # Вводим почту
        driver.find_element(*CommonElements.EMAIL_INPUT).send_keys(data.EMAIL)

        # Вводим пароль
        driver.find_element(*CommonElements.PASSWORD_INPUT).send_keys(data.PASSWORD)

        # Заходим в аккаунт
        driver.find_element(*LogInPopUp.LOGIN_BTN).click()

        # Проверяем появление аватара
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(MainPage.AVATAR_BTN)
        )

        # Выходим из аккаунта
        driver.find_element(*MainPage.LOGOUT_BTN).click()

        # Проверяем исчезновние аватара
        assert WebDriverWait(driver, 10).until_not(
            visibility_of_element_located(MainPage.AVATAR_BTN)
        )

        # Проверяем исчезновение имени
        assert WebDriverWait(driver, 10).until_not(
            visibility_of_element_located(MainPage.USER_NAME)
        )
