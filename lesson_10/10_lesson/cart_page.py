from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class CartPage(BasePage):
    """
    Класс для работы со страницей корзины покупок.
    """
    
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        
        Args:
            driver: WebDriver instance - экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self):
        """
        Нажать кнопку оформления заказа.
        """
        self.click(self.CHECKOUT_BUTTON)