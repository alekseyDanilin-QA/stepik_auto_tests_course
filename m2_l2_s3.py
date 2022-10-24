from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Read x
    # x = browser.find_element(By.XPATH,'/html/body/div/form/div[1]/label/span[2]')
    # x = browser.find_element(By.CSS_SELECTOR,'#input_value' ) #id="input_value"
    num1 = browser.find_element(By.ID, 'num1')  #id="num1"
    num2 = browser.find_element(By.ID, 'num2')  #id="num2"
    rez =  str(int(num1.text) + int(num2.text))
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(rez)
    browser.find_element(By.CSS_SELECTOR, 'form button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()