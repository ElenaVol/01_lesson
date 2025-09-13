
import pytest
import time
from selenium import webdriver
from calculator_page import CalculatorPage  

class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Настройка драйвера перед каждым тестом"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()
    
    def test_calculator_with_delay(self):
        """Тест калькулятора с задержкой 45 секунд"""
                  
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        
        calculator_page.set_delay(45)
        
       
        calculator_page.calculate_7_plus_8()
        
        
        start_time = time.time()
        timeout = 50 
        
        result = ""
        while time.time() - start_time < timeout:
            try:
                result = calculator_page.get_display_text()
                if result and result != "0":
                    break
            except:
                pass
            time.sleep(1)
        
       
        assert result == "15", f"Ожидался результат 15, но получено {result}"
        
        
        elapsed_time = time.time() - start_time
        assert elapsed_time >= 40, f"Операция выполнилась слишком быстро: {elapsed_time:.2f} секунд"
        print(f"Тест завершен за {elapsed_time:.2f} секунд, результат: {result}")