from selenium.webdriver.common.by import By
from saucedemo_base_page import BasePage

class ProductsPage(BasePage):
    # Локаторы
    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
    # Универсальный локатор для кнопок добавления в корзину
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_title_text(self):
        """Получить текст заголовка"""
        return self.get_text(self.TITLE)
    
    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        if self.is_element_present(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0
    
    def go_to_cart(self):
        """Перейти в корзину"""
        self.click(self.CART_LINK)