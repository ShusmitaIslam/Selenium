# Problem 7: Checkbox Selection

# Website:
# https://the-internet.herokuapp.com/checkboxes

# Task
# Page ওপেন করো।
# দুইটি checkbox locate করো।
# যদি প্রথম checkbox unchecked থাকে, তাহলে check করো।
# যদি দ্বিতীয় checkbox checked থাকে, তাহলে uncheck করো।
# শেষে দুইটার status print করো।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[type="Checkbox"]'))
)
if not checkboxs[0].is_selected():
    checkboxs[0].click()
    
if checkboxs[1].is_selected():
    checkboxs[1].click()
    
print("Checkbox 1:","Checked" if checkboxs[0].is_selected() else "Unchecked")
print("Checkbox 2:", "Checked" if checkboxs[1].is_selected() else "Unchecked")
      




