from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/?utm_source=chatgpt.com")

all_links = driver.find_elements(By.TAG_NAME, 'a')
for link in all_links:
    print(link.text)