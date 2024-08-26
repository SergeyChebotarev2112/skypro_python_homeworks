from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

# Переходим на страницу
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

# Добавляем элементы 5 раз
for i in range(5):
    # Находим кнопку Add Element и нажимаем на нее
    add_button = driver.find_element(
        By.XPATH, '//button[text()="Add Element"]')
    add_button.click()

sleep(5)

# Собираем список кнопок Delete
delete_buttons_driver = driver.find_elements(
    By.XPATH, '//button[text()="Delete"]')

# Выводим размер списка
print("Размер списка кнопок Delete:", len(delete_buttons_driver))

# Закрываем браузер
driver.quit()
