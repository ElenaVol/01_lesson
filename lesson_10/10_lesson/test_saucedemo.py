import pytest
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.feature("Оформление заказа")
class TestSauceDemo:
    """
    Тесты для оформления заказа в интернет-магазине SauceDemo.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Настройка драйвера перед каждым тестом.
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()
    
    @allure.title("Проверка итоговой суммы заказа")
    @allure.description("Тест проверяет корректность расчета итоговой суммы при оформлении заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_checkout_total_amount(self):
        """Тест проверки итоговой суммы заказа"""
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        
        with allure.step("Авторизация пользователя"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Добавление товаров в корзину"):
            backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
            tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
            onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
            
            products_page.click(backpack_add_button)
            products_page.click(tshirt_add_button)
            products_page.click(onesie_add_button)
            
            allure.attach("Добавлены товары: Backpack, Bolt T-Shirt, Onesie", name="Добавленные товары")
        
        with allure.step("Переход в корзину"):
            products_page.go_to_cart()
        
        with allure.step("Начало оформления заказа"):
            cart_page.click_checkout()
        
        with allure.step("Заполнение данных для оформления"):
            checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
            checkout_page.click_continue()
        
        with allure.step("Получение итоговой суммы"):
            total_text = checkout_page.get_total_text()
            allure.attach(f"Итоговая сумма: {total_text}", name="Сумма заказа")
        
        with allure.step("Проверка корректности суммы"):
            assert "$58.29" in total_text, f"Ожидалась сумма $58.29, но получено: {total_text}"
            allure.attach("Сумма заказа корректна: $58.29", name="Результат проверки")
       