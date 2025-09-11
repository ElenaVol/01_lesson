from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage  

class ProductsPage(BasePage):
    # Локаторы
    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
    # Локаторы товаров
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_title(self):
        return self.get_text(self.TITLE)
    
    def get_cart_items_count(self):
        if self.is_element_present(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0
    
    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_BUTTON)
        return self
    
    def add_bolt_tshirt_to_cart(self):
        self.click(self.BOLT_TSHIRT_ADD_BUTTON)
        return self
    
    def add_onesie_to_cart(self):
        self.click(self.ONESIE_ADD_BUTTON)
        return self
    
    def go_to_cart(self):
        self.click(self.CART_LINK)