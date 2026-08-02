# Problem 8: Dropdown Selection

# Website:
# https://the-internet.herokuapp.com/dropdown

# Task
# Dropdown locate করো।
# নিচের তিনভাবে option select করো:
# Visible Text
# Value
# Index
# প্রতিবার কোন option selected হয়েছে, print করো।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = driver.find_element(By.ID, "dropdown")

select = Select(dropdown)

select.select_by_visible_text("Option 1")
print(select.first_selected_option.text)

select.select_by_value("2")
print(select.first_selected_option.text)

select.select_by_index(2)
print(select.first_selected_option.text)

driver.quit()