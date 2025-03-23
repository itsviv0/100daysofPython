from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service)
driver.get("https://x.com/i/flow/login")

time.sleep(5)
# Select the input field using the name attribute
input_field = driver.find_element(By.NAME, "text")

# Perform actions (e.g., sending text)
input_field.send_keys("Hello, Selenium!")

time.sleep(5)
# Optional: Close the browser
# driver.quit()
