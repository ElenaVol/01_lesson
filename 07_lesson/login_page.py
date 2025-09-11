from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage  

class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self
    
    def enter_username(self, username):
        self.send_keys(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)
        return self
    
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()