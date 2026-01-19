from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import *
from tests.conftest import *

# Регистрация с валидными данными
def test_success_register():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")
    wait = WebDriverWait(driver, 10)

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, REGISTER_SUBMIT_BUTTON)))

# Имя
    driver.find_element(By.XPATH, REGISTER_NAME_INPUT).send_keys("Иван")
    
# Email
    driver.find_element(By.XPATH, REGISTER_EMAIL_INPUT).send_keys(generate_email())

# Пароль (невалидный)
    driver.find_element(By.XPATH, REGISTER_PASSWORD_INPUT).send_keys(generate_valid_password())

# Кнопка "Зарегистрироваться"
    driver.find_element(By.XPATH, REGISTER_SUBMIT_BUTTON).click()

# Ожидание перехода на страницу авторизации
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, SUBMIT_LOGIN_BUTTON)))

# Проверь, что в текущий url = "https://stellarburgers.education-services.ru/login"
    assert driver.current_url == 'https://stellarburgers.education-services.ru/login'

# Закрыть браузер
    driver.quit()



# Регистрация с невалидной длиной пароля
def test_register_with_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")
    wait = WebDriverWait(driver, 10)

# Ожидание загрузки
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, REGISTER_SUBMIT_BUTTON)))

# Имя
    driver.find_element(By.XPATH, REGISTER_NAME_INPUT).send_keys("Иван")
    
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

# Закрыть браузер
    driver.quit()
