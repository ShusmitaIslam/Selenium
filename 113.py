# Problem 13: JavaScript Prompt

# Website:
# https://the-internet.herokuapp.com/javascript_alerts

# Task
# Click for JS Prompt button-এ click করো।
# Alert-এ নিজের নাম লিখো (যেমন: Shusmita)।
# OK চাপো।
# নিচের result message print করো।
# Verify করো message-এ তোমার নাম আছে।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

js_prompt_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[text()="Click for JS Prompt"]'))
)
js_prompt_button.click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.send_keys("Shusmita")
alert.accept()

result = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'result'))
)
print(result.text)

assert "Shusmita" in result.text, "Name is not present in the message."

driver.quit()

