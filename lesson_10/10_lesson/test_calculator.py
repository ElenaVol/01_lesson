
import pytest
import time
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.feature("Калькулятор с задержкой")
class TestCalculator:
    """
    Тесты для калькулятора с задержкой вычислений.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Настройка драйвера перед каждым тестом.
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()
    
    @allure.title("Тест калькулятора с задержкой 45 секунд")
    @allure.description("Проверка работы калькулятора с установленной задержкой вычислений 45 секунд")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculator_with_delay(self):
        """Тест калькулятора с задержкой 45 секунд"""
        calculator_page = CalculatorPage(self.driver)
        
        with allure.step("Открыть страницу калькулятора"):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        with allure.step("Установить задержку вычислений"):
            calculator_page.set_delay(45)
        
        with allure.step("Выполнить операцию 7 + 8"):
            calculator_page.calculate_7_plus_8()
        
        with allure.step("Ожидать результат вычислений"):
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
        
        with allure.step("Проверить результат вычислений"):
            allure.attach(f"Полученный результат: {result}", name="Результат вычислений")
            assert result == "15", f"Ожидался результат 15, но получено {result}"
        
        with allure.step("Проверить время выполнения операции"):
            elapsed_time = time.time() - start_time
            allure.attach(f"Время выполнения: {elapsed_time:.2f} секунд", name="Время выполнения")
            assert elapsed_time >= 40, f"Операция выполнилась слишком быстро: {elapsed_time:.2f} секунд"
            
        allure.attach(f"Тест завершен за {elapsed_time:.2f} секунд, результат: {result}", 
                     name="Итог теста")