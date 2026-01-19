from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import *
from tests.conftest import *

# Вход по кнопке «Войти в аккаунт» на главной
def test_login_from_main_page_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")
    wait = WebDriverWait(driver, 10)

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_BUTTON)))

# Кнопка "Войти в аккаунт"
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Email
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys('maklakov.ivan0@gmail.com')

# Пароль 
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys('123456')

# Кнопка "Войти"
    driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешной авторизации по наличии кнопки "Оформить заказ"
    assert driver.find_element(By.XPATH, MAKE_ORDER_BUTTON)

# Закрыть браузер
    driver.quit()


# Вход через кнопку «Личный кабинет»
def test_login_via_profile_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")
    wait = WebDriverWait(driver, 10)

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_BUTTON)))

# Кнопка "Личный кабинет"
    driver.find_element(By.XPATH, PROFILE_BUTTON).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Email
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys('maklakov.ivan0@gmail.com')

# Пароль 
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys('123456')

# Кнопка "Войти"
    driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешной авторизации по наличии кнопки "Оформить заказ"
    assert driver.find_element(By.XPATH, MAKE_ORDER_BUTTON)

# Закрыть браузер
    driver.quit()


# Вход через кнопку в форме регистрации
def test_login_from_registration_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")
    wait = WebDriverWait(driver, 10)

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, REGISTER_SUBMIT_BUTTON)))

# Кнопка "Войти"
    driver.find_element(By.XPATH, LOGIN_FROM_REGISTER_LINK).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Email
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys('maklakov.ivan0@gmail.com')

# Пароль 
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys('123456')

# Кнопка "Войти"
    driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешной авторизации по наличии кнопки "Оформить заказ"
    assert driver.find_element(By.XPATH, MAKE_ORDER_BUTTON)

# Закрыть браузер
    driver.quit()


# Вход через кнопку в форме восстановления пароля
def test_login_from_forgot_password_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    wait = WebDriverWait(driver, 10)

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, FORGOT_PASSWORD_SUBMIT_BUTTON)))

# Кнопка "Войти"
    driver.find_element(By.XPATH, LOGIN_FROM_FORGOT_PASSWORD_LINK).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Email
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys('maklakov.ivan0@gmail.com')

# Пароль 
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys('123456')

# Кнопка "Войти"
    driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешной авторизации по наличии кнопки "Оформить заказ"
    assert driver.find_element(By.XPATH, MAKE_ORDER_BUTTON)

# Закрыть браузер
    driver.quit()