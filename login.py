from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_object = Service(executable_path="C:/Users/ASUS/Desktop/V&V Wizards/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

driver.get('https://localhost:7080/')
email_field = driver.find_element(By.ID, "Email")
email_field.send_keys("ayse.hanim@gmail.com")
password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("87654321")
login_button = driver.find_element(By.CLASS_NAME, "form-submit")
login_button.click()

# print("For picture button(Enable): ",login_button.is_displayed())
# print("For picture button(Display): ",login_button.is_enabled())

# link_field = driver.find_element(By.CLASS_NAME, "signup-image-link")
# link_field.click()
# print("For link(Enable): ",link_field.is_displayed())
# print("For link(Display): ",link_field.is_enabled())

time.sleep(20)