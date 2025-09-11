
from selenium.webdriver.common.by import By
from base_page import BasePage  

class CalculatorPage(BasePage):
   
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    DISPLAY = (By.CSS_SELECTOR, ".screen")
    
   
    BUTTON_0 = (By.XPATH, "//span[text()='0']")
    BUTTON_1 = (By.XPATH, "//span[text()='1']")
    BUTTON_2 = (By.XPATH, "//span[text()='2']")
    BUTTON_3 = (By.XPATH, "//span[text()='3']")
    BUTTON_4 = (By.XPATH, "//span[text()='4']")
    BUTTON_5 = (By.XPATH, "//span[text()='5']")
    BUTTON_6 = (By.XPATH, "//span[text()='6']")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_9 = (By.XPATH, "//span[text()='9']")
    
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_MINUS = (By.XPATH, "//span[text()='-']")
    BUTTON_MULTIPLY = (By.XPATH, "//span[text()='×']")
    BUTTON_DIVIDE = (By.XPATH, "//span[text()='÷']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    BUTTON_CLEAR = (By.XPATH, "//span[text()='C']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def set_delay(self, delay_value):
        """Установить значение задержки"""
        self.send_keys(self.DELAY_INPUT, str(delay_value))
    
    def get_display_text(self):
        """Получить текст с дисплея калькулятора"""
        return self.get_text(self.DISPLAY)
    
    def click_button(self, button_locator):
        """Нажать кнопку по локатору"""
        self.click(button_locator)
    
    # Методы для нажатия конкретных кнопок
    def click_0(self):
        self.click_button(self.BUTTON_0)
    
    def click_1(self):
        self.click_button(self.BUTTON_1)
    
    def click_2(self):
        self.click_button(self.BUTTON_2)
    
    def click_3(self):
        self.click_button(self.BUTTON_3)
    
    def click_4(self):
        self.click_button(self.BUTTON_4)
    
    def click_5(self):
        self.click_button(self.BUTTON_5)
    
    def click_6(self):
        self.click_button(self.BUTTON_6)
    
    def click_7(self):
        self.click_button(self.BUTTON_7)
    
    def click_8(self):
        self.click_button(self.BUTTON_8)
    
    def click_9(self):
        self.click_button(self.BUTTON_9)
    
    def click_plus(self):
        self.click_button(self.BUTTON_PLUS)
    
    def click_minus(self):
        self.click_button(self.BUTTON_MINUS)
    
    def click_multiply(self):
        self.click_button(self.BUTTON_MULTIPLY)
    
    def click_divide(self):
        self.click_button(self.BUTTON_DIVIDE)
    
    def click_equals(self):
        self.click_button(self.BUTTON_EQUALS)
    
    def click_clear(self):
        self.click_button(self.BUTTON_CLEAR)
    
    def calculate_7_plus_8(self):
        """Выполнить операцию 7 + 8"""
        self.click_clear() 
        self.click_7()
        self.click_plus()
        self.click_8()
        self.click_equals()