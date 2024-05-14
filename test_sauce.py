from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from time import sleep
import pytest
#import openpyxl

class Test_Sauce:
    def setup_method(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        #Her test bitiminde çalışır
        self.driver.quit()


    def test_password_and_username_empty(self):
        loginButton = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()

        errormessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errormessage.text == "Epic sadface: Username is required"
        
    

    def getData(): # Bir anatasyon içinde çağıracağım bir fonksiyon varsa ona 'self' parametresi verilmez
        
        return [("abc"),("1"),("deneme")]


    @pytest.mark.parametrize("userName", getData())
    def test_only_password_empty(self, userName):
        userNameInput = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        userNameInput.send_keys(userName)

        loginButton = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errormessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errormessage.text == "Epic sadface: Password is required"
        
    @pytest.mark.skip
    def test_locked_out_user(self):
        userNameInput = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        userNameInput.send_keys("standart_user")
        passwordInput = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_user")

        loginButton = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errormessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errormessage.text == "Epic sadface: Sorry, this user has been locked out."
        
    @pytest.mark.skip
    def test_count_products(self):
        userNameInput = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        userNameInput.send_keys("standart_user")
        passwordInput = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_user")

        loginButton = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
       # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='item_4_title_link']/div")))
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(elements) == 6
        
    @pytest.mark.skip
    def test_add_cart(self):
       # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='login-button']")))
        username = self.driver.find_element(By.XPATH, "//*[@id='user-name']")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.XPATH, "//*[@id='password']")
        password.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        loginbutton.click()
       # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='item_4_title_link']/div")))
        addcartbutton = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
        addcartbutton.click()
        count = self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span")
        assert count.text == "1"
        




