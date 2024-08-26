from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

# Введите имя пользователя
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("tomsmith")

# Введите пароль
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("SuperSecretPassword!")

sleep(3)

# Нажмите кнопку Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

sleep(3)

driver.quit()
