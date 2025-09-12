from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage

class CheckoutPage(BasePage):
    
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    
   
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Заполнить форму оформления заказа"""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)
    
    def click_continue(self):
        """Нажать кнопку Continue"""
        self.click(self.CONTINUE_BUTTON)
    
    def get_total_text(self):
        """Получить итоговую сумму"""
        return self.get_text(self.TOTAL)
    
    def click_finish(self):
        """Нажать кнопку Finish"""
        self.click(self.FINISH_BUTTON)