import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

service_object = Service(executable_path="C:/Users/ASUS/Desktop/V&V Wizards/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

driver.get('https://localhost:7080/Article/AddNewBlog')
header_field = driver.find_element(By.NAME, "Header")
header_field.send_keys("Merhaba Blog")
content_field = driver.find_element(By.NAME, "Content")
content_field.send_keys("Here is Blog's content. You can write any article here.")
select_Font_Size = driver.find_element(By.ID,"FontSize" )
select_Font_Size.send_keys("16px")
select_Font_Family = driver.find_element(By.ID,"FontFamily")
select_Font_Family.send_keys("Poppins")
select_Font_Color = driver.find_element(By.ID,"FontColor" )
select_Font_Color.send_keys("Black")
save_button = driver.find_element(By.CLASS_NAME, "btn-success")
#save_button.click()

time.sleep(100)