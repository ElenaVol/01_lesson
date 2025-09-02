from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()  

try:

    driver.get("http://uitestingplayground.com/textinput")
    
    
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()  
    input_field.send_keys("SkyPro")  
    
    
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    blue_button.click()
    
    
    updated_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "updatingButton"))
    )
    button_text = updated_button.text
    print(button_text)  

finally:
    driver.quit()