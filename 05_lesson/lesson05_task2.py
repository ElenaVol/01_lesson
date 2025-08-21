from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    
    driver.get("http://uitestingplayground.com/dynamicid")
    
   
    time.sleep(2)
    
   
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    
 
    blue_button.click()
    
    print("Успешно кликнули на синюю кнопку с динамическим ID!")
    
   
    time.sleep(2)
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
   
    driver.quit()