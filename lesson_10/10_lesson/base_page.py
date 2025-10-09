from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """
    Базовый класс для всех страниц, содержащий общие методы для работы с веб-элементами.
    """
    
    def __init__(self, driver):
        """
        Инициализация базовой страницы.
        
        Args:
            driver: WebDriver instance - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """
        Найти элемент на странице с ожиданием.
        
        Args:
            locator: tuple - локатор элемента в формате (By, selector)
            
        Returns:
            WebElement - найденный веб-элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """
        Найти все элементы на странице с ожиданием.
        
        Args:
            locator: tuple - локатор элементов в формате (By, selector)
            
        Returns:
            list[WebElement] - список найденных веб-элементов
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """
        Кликнуть по элементу.
        
        Args:
            locator: tuple - локатор элемента в формате (By, selector)
        """
        element = self.find_element(locator)
        element.click()
    
    def send_keys(self, locator, text):
        """
        Ввести текст в элемент.
        
        Args:
            locator: tuple - локатор элемента в формате (By, selector)
            text: str - текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """
        Получить текст элемента.
        
        Args:
            locator: tuple - локатор элемента в формате (By, selector)
            
        Returns:
            str - текст элемента
        """
        element = self.find_element(locator)
        return element.text
    
   