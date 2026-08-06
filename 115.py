# Problem 15: Mouse Hover

# Website:
# https://the-internet.herokuapp.com/hovers

# Task
# প্রথম user image-এর উপর mouse hover করো।
# Hover করার পরে যে username দেখা যায়, সেটা print করো।
# দ্বিতীয় image-এর জন্যও একই কাজ করো।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/hovers")

first_user = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]')
action = ActionChains(driver)
action.move_to_element(first_user).perform()
first_username = first_user.find_element(By.TAG_NAME, 'h5')
print(first_username.text)

second_user = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]')
action.move_to_element(second_user).perform()
second_username = second_user.find_element(By.TAG_NAME, 'h5')
print(second_username.text)

driver.quit()

