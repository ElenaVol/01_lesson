from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage  

class CartPage(BasePage):
    # Локаторы
    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_title(self):
        return self.get_text(self.TITLE)
    
    def get_cart_items_count(self):
        return len(self.find_elements(self.CART_ITEMS))
    
    def get_item_names(self):
        items = self.find_elements((By.CLASS_NAME, "inventory_item_name"))
        return [item.text for item in items]
    
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)