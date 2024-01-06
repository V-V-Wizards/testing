from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_object = Service(executable_path="C:/Users/ASUS/Desktop/V&V Wizards/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

driver.get('https://localhost:7080/Account/SignUp')

#in register
firtName_field = driver.find_element(By.ID, "FirstName")
firtName_field.send_keys("ali")
lastName_field = driver.find_element(By.ID, "LastName")
lastName_field.send_keys("bey")
email_field = driver.find_element(By.ID, "Email")
email_field.send_keys("ayse.hanim@gmail.com")
password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("1234567890")
register_button = driver.find_element(By.CLASS_NAME, "form-submit")
register_button.click()



# try:
#     find_picture = driver.find_element(By.XPATH, "//img[@alt='sing up image' and @src='/images/for-sign-up.jpg']")
#     print("Picture was found.")
# except:
#     print("Picture was not found!")


# try:
#     image_element = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//img[@alt='sing up image' and @src='/images/for-sign-up.jpg']"))
#     )
#     print("Picture was found.")
# except:
#     print("Picture was not found!")
time.sleep(10)


