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
       
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        
      
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
       
        backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        
        products_page.click(backpack_add_button)
        products_page.click(tshirt_add_button)
        products_page.click(onesie_add_button)
        
       
        products_page.go_to_cart()
        
       
        cart_page.click_checkout()
        
       
        checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
        checkout_page.click_continue()
        
    
        total_text = checkout_page.get_total_text()
        
      
        assert "$58.29" in total_text, f"Ожидалась сумма $58.29, но получено: {total_text}"
        
       