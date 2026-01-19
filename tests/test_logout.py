from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import *
from tests.conftest import *

# Выход из аккаунта
def test_logout():
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

# Кнопка "Личный кабинет"
    driver.find_element(By.XPATH, PROFILE_BUTTON_AUTH).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SAVE_PROFILE_BUTTON)))

# Кнопка "Выход"
    driver.find_element(By.XPATH, LOGOUT_BUTTON).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Проверка успешного перехода в личный кабинет
    assert driver.find_element(By.XPATH, SUBMIT_LOGIN_BUTTON)

# Закрыть браузер
    driver.quit()
