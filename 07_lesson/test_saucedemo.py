import pytest
import time
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()
    
    def test_checkout_total_amount(self):
        # Создаем объекты страниц
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        
        # 1. Открываем сайт и авторизуемся
        login_page.open().login("standard_user", "secret_sauce")
        
        # 2. Добавляем товары в корзину
        products_page.add_backpack_to_cart()
        products_page.add_bolt_tshirt_to_cart()
        products_page.add_onesie_to_cart()
        
        # 3. Переходим в корзину
        products_page.go_to_cart()
        
        # 4. Нажимаем кнопку Checkout
        cart_page.click_checkout()
        
        # 5. Заполняем форму оформления заказа
        checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
        checkout_page.click_continue()
        
        # 6. Получаем итоговую сумму
        total_text = checkout_page.get_total()
        
        # 7. Проверяем итоговую сумму
        assert "$58.29" in total_text, f"Ожидалась сумма $58.29, но получено: {total_text}"
        
        print(f"Total: {total_text}")