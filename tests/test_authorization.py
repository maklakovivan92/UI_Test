from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import *
from tests.conftest import *
from tests.data import *


class TestAuthorization:

# Вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page_button(self, driver):
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
        visible_element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешной авторизации по наличии кнопки "Оформить заказ"
        assert visible_element.is_displayed()




# Вход через кнопку «Личный кабинет»
    def test_login_via_profile_button(self, driver):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_BUTTON)))

# Кнопка "Личный кабинет"
        driver.find_element(By.XPATH, PROFILE_BUTTON).click()

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Email
        driver.find_element(By.XPATH, EMAIL_INPUT).send_keys(authorization_email)

# Пароль 
        driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(authorization_password)

# Кнопка "Войти"
        driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON).click()

# Ожидание загрузки
        visible_element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешной авторизации по наличии кнопки "Оформить заказ"
        assert visible_element.is_displayed()




# Вход через кнопку в форме регистрации
    def test_login_from_registration_form(self, driver):
        driver.get(registration_url)
        wait = WebDriverWait(driver, 10)

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, REGISTER_SUBMIT_BUTTON)))

# Кнопка "Войти"
        driver.find_element(By.XPATH, LOGIN_FROM_REGISTER_LINK).click()

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Email
        driver.find_element(By.XPATH, EMAIL_INPUT).send_keys(authorization_email)

# Пароль 
        driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(authorization_password)

# Кнопка "Войти"
        driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON).click()

# Ожидание загрузки
        visible_element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешной авторизации по наличии кнопки "Оформить заказ"
        assert visible_element.is_displayed()




# Вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_form(self, driver):
        driver.get(forgot_your_password_url)
        wait = WebDriverWait(driver, 10)

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, FORGOT_PASSWORD_SUBMIT_BUTTON)))

# Кнопка "Войти"
        driver.find_element(By.XPATH, LOGIN_FROM_FORGOT_PASSWORD_LINK).click()

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Email
        driver.find_element(By.XPATH, EMAIL_INPUT).send_keys(authorization_email)

# Пароль 
        driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(authorization_password)

# Кнопка "Войти"
        driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON).click()

# Ожидание загрузки
        visible_element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешной авторизации по наличии кнопки "Оформить заказ"
        assert visible_element.is_displayed()

