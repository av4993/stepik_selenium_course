from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '//button[text()="I want to go on a magical journey!"]')
    button.click() 
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(0.5)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    time.sleep(0.5)
    button1 = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button1.click()
    
finally:
    time.sleep(10)
    
    browser.quit()      