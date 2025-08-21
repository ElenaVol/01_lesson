from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)
    
   
    input_field = driver.find_element(By.TAG_NAME, "input")
    
    input_field.send_keys("Sky")
    print("Введено: Sky")
    time.sleep(1)
    
    input_field.clear()
    print("Поле очищено")
    time.sleep(1)
    
    input_field.send_keys("Pro")
    print("Введено: Pro")
    time.sleep(1)
    
finally:
    driver.quit()
    print("Браузер закрыт")