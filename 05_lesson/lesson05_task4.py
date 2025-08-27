from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)
    
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    time.sleep(2)
    
  
    flash_text = driver.find_element(By.ID, "flash").text.strip()
    print("Сообщение об успехе:", flash_text)
    
finally:
    driver.quit()
