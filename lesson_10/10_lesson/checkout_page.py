from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
import allure


class CheckoutPage(BasePage):
    """
    Класс для работы со страницей оформления заказа.
    """
    
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        
        Args:
            driver: WebDriver instance - экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Заполнить форму оформления заказа: {first_name} {last_name}, {postal_code}")
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """
        Заполнить форму оформления заказа.
        
        Args:
            first_name: str - имя
            last_name: str - фамилия
            postal_code: str - почтовый индекс
        """
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)
    
    @allure.step("Нажать кнопку продолжения оформления заказа")
    def click_continue(self):
        """
        Нажать кнопку продолжения оформления заказа.
        """
        self.click(self.CONTINUE_BUTTON)
    
    @allure.step("Ожидание появления итоговой суммы")
    def wait_total_visible(self, timeout=10):
        """
        Ожидать появления итоговой суммы на странице.
        
        Args:
            timeout: int - время ожидания в секундах (по умолчанию 10)
        """
        self.wait.until(EC.presence_of_element_located(self.TOTAL))
    
    @allure.step("Получить итоговую сумму заказа")
    def get_total_text(self):
        """
        Получить текст с итоговой суммой заказа.
        
        Returns:
            str - текст итоговой суммы
        """
        return self.get_text(self.TOTAL)