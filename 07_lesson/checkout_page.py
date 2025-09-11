from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage  

class CheckoutPage(BasePage):
    # Локаторы формы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    
    # Локаторы итоговой страницы
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        return self
    
    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        return self
    
    def enter_postal_code(self, postal_code):
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)
        return self
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        return self
    
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
    
    def get_item_total(self):
        return self.get_text(self.ITEM_TOTAL)
    
    def get_tax(self):
        return self.get_text(self.TAX)
    
    def get_total(self):
        return self.get_text(self.TOTAL)