# Problem 11: JavaScript Alert

# Website:
# https://the-internet.herokuapp.com/javascript_alerts

# Task
# Page ওপেন করো।
# Click for JS Alert button-এ click করো।
# Alert accept করো।
# নিচের result message print করো।

# Verify করো message হলো:

# You successfully clicked an alert
# Concept
# driver.switch_to.alert
# accept()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

js_alert_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/ul/li[1]/button'))
)
js_alert_button.click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

result_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'result'))
)

print(result_message.text)

assert result_message.text == "You successfully clicked an alert", "Result Message is not matched."




