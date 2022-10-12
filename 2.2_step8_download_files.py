import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Captain")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Nemo")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("cn@nautilus.oc")
    time.sleep(0.5)
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')           
    input4.send_keys(file_path)   
    time.sleep(0.5)
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
    
finally:
    time.sleep(5)
    
    browser.quit()  
    
