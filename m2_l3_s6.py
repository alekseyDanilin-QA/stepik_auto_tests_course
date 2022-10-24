from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'div button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)
    x = browser.find_element(By.ID, 'input_value')  #id="treasure"
    y = x.text
    rez =  str(math.log(abs(12*math.sin(int(y)))))
    #write calculate
    browser.find_element(By.ID, 'answer').send_keys(rez)
    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(10)
    browser.quit()