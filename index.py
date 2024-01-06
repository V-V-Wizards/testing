from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_object = Service(executable_path="C:/Users/ASUS/Desktop/V&V Wizards/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

#driver.get('https://localhost:7080/Article/Index')
# logout_button = driver.find_element(By.CLASS_NAME, "nav-link")
# logout_button.click()
driver.get('https://localhost:7080')
email_field = driver.find_element(By.ID, "Email")
email_field.send_keys("ayse.hanim@gmail.com")
password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("12345678")
login_button = driver.find_element(By.CLASS_NAME, "form-submit")
login_button.click()

blog_button = driver.find_element(By.CLASS_NAME, "navbar-brand")
blog_button.click()
print(blog_button.is_enabled())
print(blog_button.is_displayed())

# driver.get('https://localhost:7080/Article/AddNewBlog')
# blog_button = driver.find_element(By.CLASS_NAME, "navbar-brand")
# blog_button.click()
#print(blog_button.is_enabled())
#print(blog_button.is_displayed())

time.sleep(100)