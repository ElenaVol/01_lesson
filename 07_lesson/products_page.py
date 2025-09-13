from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage

class ProductsPage(BasePage):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def go_to_cart(self):
        self.click(self.CART_LINK)