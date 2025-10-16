from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

import data
from locators import MainPage, LogInPopUp, CommonElements, PublicationForm, type_choose


class TestPublicationCreate:

    def test_non_registrated_user_announcement_create(self, driver):

        # Открываем бразуер и переходим на нужный сайт
        driver.get(data.URL)

        # Нажимаем на размещение объявления
        driver.find_element(*MainPage.PUBLISH_BTN).click()

        # Проверяем появление всплывающего окна
        assert WebDriverWait(driver, 10).until(
            visibility_of_element_located(CommonElements.POPUP_HEADER)).is_displayed()

        # Проверяем заголовок окна
        assert 'Чтобы разместить объявление, авторизуйтесь' in driver.find_element(*CommonElements.POPUP_HEADER).text

    def test_registrated_user_announcement_create(self, driver):
        title = "Тарелки"
        description = "Дорогие тарелки"
        price = "5656"
        value = "Новый"
        type = "Книги"
        city = "Санкт-Петербург"

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

        # Нажимаем на размещение объявления
        driver.find_element(*MainPage.PUBLISH_BTN).click()

        # Проверяем появление всплывающего окна
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(CommonElements.POPUP_HEADER)).is_displayed()

        # Устанавливаем название
        driver.find_element(*PublicationForm.TITLE).send_keys(title)

        # Устанавливаем описание
        driver.find_element(*PublicationForm.DESCRIPTION).send_keys(description)

        # Устанавливаем цену
        driver.find_element(*PublicationForm.PRICE).send_keys(price)

        # Открываем выпадающий список с типом
        driver.find_element(*PublicationForm.DROPDOWN[0]).click()

        # Выбираем пункт
        type_choose(driver, type).click()

        # Открываем выпадающий список с городом
        driver.find_element(*PublicationForm.DROPDOWN[1]).click()

        # Выбираем город
        type_choose(driver, city).click()

        # Создаем объявление
        driver.find_element(*PublicationForm.PUBLISH_BTN).click()

        # Нажимаем на свой аватар
        driver.find_element(*MainPage.AVATAR_BTN).click()

        # Проверяем, что объявление в профиле
        assert WebDriverWait(driver, 10).until(
            visibility_of_element_located(MainPage.PUBLICATION_ELEMENT)
        )
