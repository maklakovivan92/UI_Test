from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import *
from tests.conftest import *
from tests.data import *

class TestLogout:
# Выход из аккаунта
    def test_logout(self, driver):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_BUTTON)))

# Кнопка "Войти в аккаунт"
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Email
        driver.find_element(By.XPATH, EMAIL_INPUT).send_keys(authorization_email)

# Пароль 
        driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(authorization_password)

# Кнопка "Войти"
        driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON).click()

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Кнопка "Личный кабинет"
        driver.find_element(By.XPATH, PROFILE_BUTTON_AUTH).click()

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SAVE_PROFILE_BUTTON)))

# Кнопка "Выход"
        driver.find_element(By.XPATH, LOGOUT_BUTTON).click()

# Ожидание загрузки
        visible_element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Проверка успешного перехода в личный кабинет
        assert visible_element.is_displayed()


