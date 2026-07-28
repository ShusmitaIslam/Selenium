import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.youtube.com/")
time.sleep(3)

driver.get("https://www.google.com/")
time.sleep(2)

driver.get("https://www.facebook.com/")
time.sleep(2)

#current url check
print(driver.current_url)

print(driver.title)

driver.quit()