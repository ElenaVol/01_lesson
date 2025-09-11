from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestSlowCalculator:
    
    @pytest.fixture(scope="function")
    def driver(self):
       
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_slow_calculator(self, driver):
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        
        delay_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")
        
       
        buttons_to_click = ["7", "+", "8", "="]
        
        for button_text in buttons_to_click:
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']"))
            )
            button.click()
        
       
        result_display = WebDriverWait(driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        
       