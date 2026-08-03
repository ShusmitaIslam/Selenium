# Problem 10: Explicit Wait

# Website:
# https://the-internet.herokuapp.com/dynamic_loading

# Task
# "Example 1" এ click করো।
# "Start" button click করো।
# Explicit Wait ব্যবহার করে "Hello World!" message-এর জন্য অপেক্ষা করো।
# Message print করো।
# Verify করো message ঠিক আছে কিনা।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading")

example_one = driver.find_element(By.XPATH, '//*[@id="content"]/div/a[1]')
example_one.click()

start_button = driver.find_element(By.XPATH, '//*[@id="start"]/button')
start_button.click()

message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4'))
)
print("Message: ", message.text)

assert "Hello World!" in message.text, "Message is not correct."