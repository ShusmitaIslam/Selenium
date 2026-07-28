from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.heroku.com/")

time.sleep(2)

assert driver.title == "Heroku | The Cloud Application Platform For Developers"

print(driver.title)

driver.quit()