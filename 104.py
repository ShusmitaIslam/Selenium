from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)
username.send_keys("tomsmith")

password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password.send_keys("SuperSecretPassword!")

login = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/button/i'))
)
login.click()

success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'flash'))
)

driver.quit()