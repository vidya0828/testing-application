        
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver
driver = webdriver.Chrome()

# URL
base_url = "https://www.demoblaze.com/"

# Function to sign up
def signup(username, password):
    driver.get(base_url)
    time.sleep(2)
    driver.find_element(By.ID, "signin2").click()
    time.sleep(2)
    driver.find_element(By.ID, "sign-username").send_keys(username)
    driver.find_element(By.ID, "sign-password").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()
    time.sleep(2)

# Function to log in
def login(username, password):
    driver.get(base_url)
    time.sleep(2)
    driver.find_element(By.ID, "login2").click()
    time.sleep(2)
    driver.find_element(By.ID, "loginusername").send_keys(username)
    driver.find_element(By.ID, "loginpassword").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    time.sleep(2)

# Function to browse products
def browse_products():
    driver.get(base_url)
    time.sleep(2)
    # Verify that products are displayed on homepage
    assert len(driver.find_elements(By.CLASS_NAME, "card-block")) > 0

# Function to add product to cart
def add_product_to_cart():
    driver.get(base_url)
    time.sleep(2)
    # Navigate to last product
    driver.find_element(By.XPATH, "//a[contains(text(),'Next')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Next')]").click()
    time.sleep(2)
    last_product = driver.find_elements(By.CLASS_NAME, "hrefch")[-1]
    last_product.click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]").click()
    time.sleep(2)

# Function to checkout
def checkout():
    driver.get(base_url)
    time.sleep(2)
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
    time.sleep(2)
    # Fill in details for checkout
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.ID, "country").send_keys("Test Country")
    driver.find_element(By.ID, "city").send_keys("Test City")
    driver.find_element(By.ID, "card").send_keys("1234567890123456")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2025")
    driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]").click()
    time.sleep(2)

# Function to logout
def logout():
    driver.find_element(By.ID, "logout2").click()
    time.sleep(2)

# Test Cases
try:
    # Signup Test Cases
    signup("testuser", "testpassword")  # Positive scenario
    signup("", "")  # Negative scenario

    # Login Test Cases
    login("testuser", "testpassword")  # Positive scenario
    login("invaliduser", "invalidpassword")  # Negative scenario

    # Product Browsing Test Case
    browse_products()

    # Add Product to Cart Test Case
    add_product_to_cart()

    # Checkout Test Cases
    checkout()  # Positive scenario
    checkout()  # Negative scenario (No products in cart)

    # Logout Test Case
    logout()

finally:
    driver.quit()