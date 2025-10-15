from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class ProductsPage(BasePage):
    """
    Класс для работы со страницей товаров.
    """
    
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
    def __init__(self, driver):
        """
        Инициализация страницы товаров.
        
        Args:
            driver: WebDriver instance - экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Перейти в корзину покупок")
    def go_to_cart(self):
        """
        Перейти в корзину покупок.
        """
        self.click(self.CART_LINK)