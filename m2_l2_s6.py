from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value')  #id="treasure"
    y = x.text
    rez =  str(math.log(abs(12*math.sin(int(y)))))
    #write calculate
    answer = browser.find_element(by=By.ID,value='answer')
    answer.send_keys(rez)
    #find checkbox "I'm the robot".
    checkbox = browser.find_element(by=By.ID,value='robotCheckbox')
    checkbox.click()
    #find radiobutton "Robots rule!"
    radiobutton = browser.find_element(by=By.ID,value='robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()