from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

def calc(a, b):
    return str(int(a) + int(b))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x1 = x1_element.text
    x2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    x2 = x2_element.text    
    y = calc(x1, x2)
    
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(y)
    
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()    
finally:
    time.sleep(5)
    
    browser.quit()

    
    