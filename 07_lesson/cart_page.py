from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage

class CartPage(BasePage):
 
    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_title_text(self):
        """Получить текст заголовка"""
        return self.get_text(self.TITLE)
    
    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        return len(self.find_elements(self.CART_ITEMS))
    
    def get_item_names(self):
        """Получить список названий товаров в корзине"""
        items = self.find_elements((By.CLASS_NAME, "inventory_item_name"))
        return [item.text for item in items]
    
    def click_checkout(self):
        """Нажать кнопку Checkout"""
        self.click(self.CHECKOUT_BUTTON)