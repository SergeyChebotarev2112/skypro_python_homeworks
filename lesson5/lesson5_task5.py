from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")

# Введите текст 1000
input_field = driver.find_element(By.TAG_NAME, 'input')
input_field.send_keys("1000")

sleep(3)

# Очистите поле
input_field.clear()

# Введите текст 999
input_field.send_keys("999")

sleep(3)

driver.quit()