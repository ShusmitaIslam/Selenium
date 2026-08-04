# Problem 12: JavaScript Confirm

# Website:
# https://the-internet.herokuapp.com/javascript_alerts

# Task
# Click for JS Confirm button-এ click করো।
# প্রথমবার Cancel করো।
# Result print করো।
# আবার button click করে এবার OK করো।
# দুইবারের result compare করো।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

js_confirm_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/ul/li[2]/button'))
)
js_confirm_button.click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.dismiss()
result1 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'result'))
)
print("After Cancel:\n", result1.text)

js_confirm_button.click()
alert.accept()
result2 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'result'))
)
print("After OK:\n", result2.text)
