import pytest
from selenium import webdriver

from helpers import generate_email, generate_password


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def generate_random_email():
    return generate_email()


@pytest.fixture
def generate_random_password():
    return generate_password()