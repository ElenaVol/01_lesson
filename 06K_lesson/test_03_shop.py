from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestSauceDemoShopping:
    
    @pytest.fixture(scope="function")
    def driver(self):
      
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_shopping_cart_total(self, driver):
        
        driver.get("https://www.saucedemo.com/")
        
        
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        
        
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        
        for product_name in products_to_add:
          
            add_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
                    f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[contains(text(), 'Add to cart')]"))
            )
            add_button.click()
        
        
        cart_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_icon.click()
        
        
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        
       
        first_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys("Иван")
        
        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Петров")
        
        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("123456")
        
       
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        
       
        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "")
        
        assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получено ${total_amount}"
        
        