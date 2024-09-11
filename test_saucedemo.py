from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestSaucedemo:
    # Написание функции авторизации для использования в тесте
    def authorize(self, driver):
        # Находим все элементы авторизации
        login = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        login.send_keys('standard_user')
        password.send_keys('secret_sauce')
        login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
        login_button.click()
    # Написание функции добавления товара и перехода в корзину для использования в тесте
    def my_cart(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt ='Sauce Labs Backpack']")))
        product = driver.find_element(By.XPATH, "//img[@alt ='Sauce Labs Backpack']")
        product.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name ='add-to-cart']")))
        cart_button = driver.find_element(By.XPATH, "//button[@name ='add-to-cart']")
        cart_button.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class ='shopping_cart_link']")))
        cart_link = driver.find_element(By.XPATH, "//a[@class ='shopping_cart_link']")
        cart_link.click()
    # Функция для оформления заказа
    def do_order(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name ='checkout']")))
        buy_button = driver.find_element(By.XPATH, "//button[@name ='checkout']")
        buy_button.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder ='First Name']")))
        your_firstname = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        your_lastname = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        your_zip_postal_cod = driver.find_element(By.XPATH, "//input[@placeholder='Zip/Postal Code']")
        your_firstname.send_keys('Testname')
        your_lastname.send_keys('learnqa')
        your_zip_postal_cod.send_keys('125212')
        next_button = driver.find_element(By.XPATH, "//input[@type ='submit']")
        next_button.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name ='finish']")))
        finish_button = driver.find_element(By.XPATH, "//button[@name ='finish']")
        finish_button.click()
    # Тест на покупку товара
    def test_shopping(self):
        url = 'https://www.saucedemo.com'
        with webdriver.Chrome() as driver:
            driver.get(url)
            # Выполняем авторизацию
            self.authorize(driver)
            # Осуществляем добавление товара и переход в корзину
            self.my_cart(driver)
            # Добавленный товар в корзине
            actual_product_in_my_cart = driver.find_element(By.XPATH, "//div[@class ='inventory_item_name']")
            # Проверяем, был ли успешно добавлен товар в корзину
            assert actual_product_in_my_cart.text == 'Sauce Labs Backpack', "Problems adding product to cart"
            # Оформляем покупку
            self.do_order(driver)
            actual_header = driver.find_element(By.XPATH, "//h2[@class ='complete-header']") # поиск элемента успешного оформления покупки
            expected_result = 'Thank you for your order!' # Ожидаемый текст заголовка после успешной покупки
            actual_result = actual_header.text # Фактический результат
            assert actual_result == expected_result, "actual_result doesn't look like expected_result" # сравнение фактического и ожидаемого результата