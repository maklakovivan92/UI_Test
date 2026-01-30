from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import *
from tests.conftest import *
from tests.data import *

class TestConstructorSection:
# Переход к разделу "Начинки"
    def test_go_to_the_filling_section(self, driver):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_BUTTON)))

# Кнопка "Начинки"
        fillings_tab = driver.find_element(By.XPATH, FILLINGS_TAB)
        fillings_tab.click()

# Проверка перехода
        assert "tab_tab_type_current" in fillings_tab.get_attribute("class")




# Переход к разделу "Соусы"
    def test_go_to_the_sauces_section(self, driver):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_BUTTON)))

# Кнопка "Соусы"
        sauces_tab = driver.find_element(By.XPATH, SAUCES_TAB)
        sauces_tab.click()

# Проверка перехода
        assert "tab_tab_type_current" in sauces_tab.get_attribute("class")




# Переход к разделу "Булки"
    def test_go_to_the_buns_section(self, driver):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

# Ожидание загрузки
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_BUTTON)))

# Кнопка "Соусы"
        sauces_tab = driver.find_element(By.XPATH, SAUCES_TAB)
        sauces_tab.click()

# Кнопка "Булки"
        buns_tab = driver.find_element(By.XPATH, BUNS_TAB)
        buns_tab.click()

# Проверка перехода
        assert "tab_tab_type_current" in buns_tab.get_attribute("class")


