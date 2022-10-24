from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input:nth-child(4)").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input:nth-child(6)").send_keys("asd")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')          # добавляем к этому пути имя файла 
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "form button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла