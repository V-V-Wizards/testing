import time

import requests
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_instance=Service(executable_path="C:/Users/ASUS/Desktop/V&V Wizards/chromedriver-win64/chromedriver.exe")
browser_instance= webdriver.Chrome(service =driver_instance)
browser_instance.get("https://localhost:7080/Article/AddNewBlog")

# Font size, font family ve font color özelliklerini kontrol etmek için bekleyin
WebDriverWait(browser_instance, 10).until(
    EC.visibility_of_element_located((By.ID, "blog-content"))
)

blog_content = browser_instance.find_element(By.ID, "blog-content")
font_size = blog_content.value_of_css_property("font-size")
font_family = blog_content.value_of_css_property("font-family")
font_color = blog_content.value_of_css_property("color")

time.sleep(100)

browser_instance.quit()
