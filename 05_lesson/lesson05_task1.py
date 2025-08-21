from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
 
    driver.get("http://uitestingplayground.com/classattr")
    
 
    time.sleep(2)
    
 
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    
   
    blue_button.click()
    
    print("Успешно кликнули на синюю кнопку!")
    
    
    time.sleep(10)
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:

    driver.quit()