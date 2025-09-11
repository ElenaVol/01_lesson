from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestDataTypesForm:
    
    @pytest.fixture(scope="function")
    def driver(self):
        
        driver = webdriver.Edge()
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_form_validation(self, driver):
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
       
        test_data = [
            ("first-name", "Иван"),
            ("last-name", "Петров"),
            ("address", "Ленина, 55-3"),
            ("e-mail", "test@skypro.com"),
            ("phone", "+7985899998787"),
            ("city", "Москва"),
            ("country", "Россия"),
            ("job-position", "QA"),
            ("company", "SkyPro")
        ]
        
        for field_id, value in test_data:
            field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            field.clear()
            field.send_keys(value)
        
        
        zip_code_field = driver.find_element(By.ID, "zip-code")
        zip_code_field.clear()
        
       
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3"))
        )
        submit_button.click()
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.is-invalid"))
        )
        
        
        zip_code_classes = zip_code_field.get_attribute("class")
        assert "is-invalid" in zip_code_classes, "Zip code поле должно иметь класс is-invalid (красный)"
        
        
        valid_fields = ["first-name", "last-name", "address", "e-mail", "phone", 
                       "city", "country", "job-position", "company"]
        
        for field_id in valid_fields:
            field = driver.find_element(By.ID, field_id)
            field_classes = field.get_attribute("class")
            assert "is-valid" in field_classes, f"Поле {field_id} должно иметь класс is-valid (зеленый)"