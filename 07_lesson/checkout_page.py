from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)
    
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
    
    def get_total_text(self):
        return self.get_text(self.TOTAL)