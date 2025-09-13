from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)