from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows?utm_source=chatgpt.com")
driver.maximize_window()
print("Parent Window Opened")

WebDriverWait(driver, 10).until(
    lambda d: "The Internet" in d.title
)
actual_title = driver.title
if "The Internet" in actual_title:
    print("Title verified")
else:
    print("Title verification failed")
    
time.sleep(2)

parent_window = driver.current_window_handle

click_here = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/a')))
click_here.click() 

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

all_windows = driver.window_handles

if len(all_windows)>1:
    print("New window opened - PASS")
else:
    print("No new window - FAIL")
    
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break

if driver.current_window_handle != parent_window:
    print("Successfully switch to child window")
else:
    print("Switch failed")

heading = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/h3')))
print("Child window heading: ", heading.text)

driver.switch_to.window(parent_window)
print("parent window title: ", driver.title)

if driver.current_window_handle == parent_window:
    print("Successfully switched to parent window")
else:
    print("Switch back failed")
    
parent_heading = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/h3')))
print("Parent window heading: ", parent_heading.text)

driver.quit()


    

    
