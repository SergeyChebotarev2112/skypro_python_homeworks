from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

# Переходим на страницу
driver.get('http://uitestingplayground.com/dynamicid')

# Находим синюю кнопку и нажимаем на нее
blue_button_driver = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
blue_button_driver.click()

# Запускаем скрипт три раза подряд
for i in range(3):
    driver.get('http://uitestingplayground.com/dynamicid')
    blue_button_driver = driver.find_element(
        By.CSS_SELECTOR, '.btn.btn-primary')
    blue_button_driver.click()
sleep(2)
# Закрываем браузер
driver.quit()
