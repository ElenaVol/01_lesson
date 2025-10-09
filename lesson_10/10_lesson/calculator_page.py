from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class CalculatorPage(BasePage):
    """
    Класс для работы со страницей калькулятора.
    """
    
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    DISPLAY = (By.CSS_SELECTOR, ".screen")
    BUTTON_LOCATOR = (By.XPATH, "//span[text()='{}']")
    
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.
        
        Args:
            driver: WebDriver instance - экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Установить задержку вычислений: {delay_value} секунд")
    def set_delay(self, delay_value):
        """
        Установить значение задержки вычислений.
        
        Args:
            delay_value: int - значение задержки в секундах
        """
        self.send_keys(self.DELAY_INPUT, str(delay_value))
    
    @allure.step("Получить текст с дисплея калькулятора")
    def get_display_text(self):
        """
        Получить текст с дисплея калькулятора.
        
        Returns:
            str - текст с дисплея
        """
        return self.get_text(self.DISPLAY)
    
    @allure.step("Нажать кнопку: '{button_text}'")
    def click_button(self, button_text):
        """
        Нажать кнопку с указанным текстом.
        
        Args:
            button_text: str - текст на кнопке
        """
        button_locator = (self.BUTTON_LOCATOR[0], self.BUTTON_LOCATOR[1].format(button_text))
        self.click(button_locator)
    
    @allure.step("Выполнить операцию: 7 + 8")
    def calculate_7_plus_8(self):
        """
        Выполнить операцию сложения 7 + 8.
        """
        self.click_button("7")
        self.click_button("+")
        self.click_button("8")
        self.click_button("=")