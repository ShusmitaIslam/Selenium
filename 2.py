from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

search_box = driver.find_element(By.ID, "APjFqb")
search_box.send_keys("What is Selenium?")
search_box.send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()