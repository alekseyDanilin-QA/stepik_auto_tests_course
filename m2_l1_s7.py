from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Read x
    # x = browser.find_element(By.XPATH,'/html/body/div/form/div[1]/label/span[2]')
    # x = browser.find_element(By.CSS_SELECTOR,'#input_value' ) #id="input_value"
    x = browser.find_element(By.ID, 'treasure')  #id="treasure"
    y = x.get_attribute("valuex")
    rez =  str(math.log(abs(12*math.sin(int(y)))))
    #write calculate
    answer = browser.find_element(by=By.ID,value='answer')
    answer.send_keys(rez)
    #find checkbox "I'm the robot".
    checkbox = browser.find_element(by=By.ID,value='robotCheckbox')
    checkbox.click()
    #find radiobutton "Robots rule!"
    radiobutton = browser.find_element(by=By.ID,value='robotsRule')
    radiobutton.click()
    #press button Submit

    butSubmit = browser.find_element(by=By.CSS_SELECTOR,value= '[class="btn btn-default"]')

    butSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()