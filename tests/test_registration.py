from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import *
from tests.conftest import *
from tests.helpers import *
from tests.data import *

class TestRegistration:
# Регистрация с валидными данными
    def test_success_register(self, driver):
        driver.get(registration_url)
        wait = WebDriverWait(driver, 10)

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, REGISTER_SUBMIT_BUTTON)))

# Имя
        driver.find_element(By.XPATH, REGISTER_NAME_INPUT).send_keys(registration_name)
    
# Email
        driver.find_element(By.XPATH, REGISTER_EMAIL_INPUT).send_keys(generate_email())

# Пароль (невалидный)
        driver.find_element(By.XPATH, REGISTER_PASSWORD_INPUT).send_keys(generate_valid_password())

# Кнопка "Зарегистрироваться"
        driver.find_element(By.XPATH, REGISTER_SUBMIT_BUTTON).click()

# Ожидание перехода на страницу авторизации
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Проверь, что в текущий url = "https://stellarburgers.education-services.ru/login"
        assert driver.current_url == login_url





# Регистрация с невалидной длиной пароля
    def test_register_with_invalid_password(self, driver):
        driver.get(registration_url)
        wait = WebDriverWait(driver, 10)

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, REGISTER_SUBMIT_BUTTON)))

# Имя
        driver.find_element(By.XPATH, REGISTER_NAME_INPUT).send_keys(registration_name)
    
# Email
        driver.find_element(By.XPATH, REGISTER_EMAIL_INPUT).send_keys(generate_email())

# Пароль (невалидный)
        driver.find_element(By.XPATH, REGISTER_PASSWORD_INPUT).send_keys(generate_invalid_password())

# Кнопка "Зарегистрироваться"
        driver.find_element(By.XPATH, REGISTER_SUBMIT_BUTTON).click()

# Ожидание ошибки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, PASSWORD_ERROR)))

# Проверка ошибки
        error = driver.find_element(By.XPATH, PASSWORD_ERROR)
        assert "Некорректный пароль" in error.text


