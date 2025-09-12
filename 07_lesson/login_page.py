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
        """Открыть страницу логина"""
        self.driver.get("https://www.saucedemo.com/")
    
    def login(self, username, password):
        """Выполнить полный процесс логина"""
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)