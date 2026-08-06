# Problem 14: File Upload

# Website:
# https://the-internet.herokuapp.com/upload

# Task
# নিজের PC থেকে একটি .txt বা .png file select করো।
# Upload button-এ click করো।
# Upload successful হয়েছে কিনা verify করো।
# Uploaded filename print করো।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

choose_file = driver.find_element(By.ID, 'file-upload')
choose_file.send_keys(r"C:\Users\Shusmita\Desktop\sample.txt")

upload = driver.find_element(By.ID, 'file-submit')
upload.click()

success_message = driver.find_element(By.XPATH, '//*[@id="content"]/div/h3')

assert "File Uploaded!" in success_message.text, "Message is showing according to the requirement."

file_name = driver.find_element(By.ID, 'uploaded-files')
assert "sample.txt" in file_name.text, "File name matched"

time.sleep(2)
driver.quit()