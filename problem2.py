from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows?utm_source=chatgpt.com")

parent = driver.current_window_handle

i=1
n=3
for i in n:
    