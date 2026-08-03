# Problem 9: Add/Remove Elements

# Website:
# https://the-internet.herokuapp.com/add_remove_elements/

# Task
# "Add Element" button ৫ বার click করো।
# কতগুলো "Delete" button তৈরি হয়েছে, print করো।
# এরপর সব Delete button remove করো।
# শেষে verify করো যে কোনো Delete button নেই।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_button_click = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/button'))
)

for i in range(5):
    add_button_click.click()
    
delete_buttons = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'added-manually'))
)
print(len(delete_buttons))

for button in delete_buttons:
    button.click()
    
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    
if len(delete_buttons) == 0:
    print("All delete buttons are removed.")
else:
    print("Some Delete buttons are still present.")
