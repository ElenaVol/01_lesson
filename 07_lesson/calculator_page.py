from selenium.webdriver.common.by import By
from base_page import BasePage

class CalculatorPage(BasePage):
  
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    DISPLAY = (By.CSS_SELECTOR, ".screen")
    
    BUTTON_LOCATOR = (By.XPATH, "//span[text()='{}']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def set_delay(self, delay_value):
        """Установить значение задержки"""
        self.send_keys(self.DELAY_INPUT, str(delay_value))
    
    def get_display_text(self):
        """Получить текст с дисплея калькулятора"""
        return self.get_text(self.DISPLAY)
    
    def click_button(self, button_text):
        """Нажать кнопку с указанным текстом"""
        button_locator = (self.BUTTON_LOCATOR[0], self.BUTTON_LOCATOR[1].format(button_text))
        self.click(button_locator)