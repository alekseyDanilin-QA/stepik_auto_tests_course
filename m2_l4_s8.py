from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, gока цена не упадёт до $100
WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
browser.find_element(By.CSS_SELECTOR, '#book').click()
time.sleep(2)
x = browser.find_element(By.ID, 'input_value')  #id="treasure"
y = x.text
rez =  str(math.log(abs(12*math.sin(int(y)))))
browser.find_element(By.ID, 'answer').send_keys(rez)
browser.find_element(By.ID, 'solve').click()
time.sleep(30)
browser.quit()
