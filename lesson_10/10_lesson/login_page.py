from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class LoginPage(BasePage):
    """
    Класс для работы со страницей авторизации.
    """
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def __init__(self, driver):
        """
        Инициализация страницы авторизации.
        
        Args:
            driver: WebDriver instance - экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Открыть страницу авторизации")
    def open(self):
        """
        Открыть страницу авторизации.
        """
        self.driver.get("https://www.saucedemo.com/")
    
    @allure.step("Выполнить авторизацию пользователем: {username}")
    def login(self, username, password):
        """
        Выполнить авторизацию.
        
        Args:
            username: str - имя пользователя
            password: str - пароль
        """
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)