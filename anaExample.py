from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service_object = Service(executable_path="C:/Users/ASUS/Desktop/V&V Wizards/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

driver.get('https://localhost:7080/Account/SignUp')

#in register
firtName_field = driver.find_element(By.ID, "FirstName")
firtName_field.send_keys("yasemin")
email_field = driver.find_element(By.ID, "Email")
email_field.send_keys("yasemin@gmail.com")
password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("12345678")
register_button = driver.find_element(By.CLASS_NAME, "form-submit")
register_button.click()
time.sleep(10)


