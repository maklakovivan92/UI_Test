from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import *
from tests.conftest import *

# Переход по клику на «Личный кабинет»
def test_go_to_your_personal_account():
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

# Проверка успешного перехода в личный кабинет
    assert driver.find_element(By.XPATH, SAVE_PROFILE_BUTTON)

# Закрыть браузер
    driver.quit()


# переход по клику на логотип Stellar Burgers из личного кабинета
def test_access_to_the_designer_via_the_logo():
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

# Логотип "Stellar Burgers"
    driver.find_element(By.XPATH, LOGO_BUTTON).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешного перехода в конструктор из личного кабинета
    assert driver.find_element(By.XPATH, MAKE_ORDER_BUTTON)

# Закрыть браузер
    driver.quit()


# переход по клику на «Конструктор» из личного кабинета
def test_go_to_the_designer_via_the_designer_button():
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

# Кнопка "Конструктор"
    driver.find_element(By.XPATH, CONSTRUCTOR_BUTTON).click()

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, MAKE_ORDER_BUTTON)))

# Проверка успешного перехода в конструктор из личного кабинета
    assert driver.find_element(By.XPATH, MAKE_ORDER_BUTTON)

# Закрыть браузер
    driver.quit()
    