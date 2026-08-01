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

old_url = driver.current_url

login = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/button'))
)
login.click()

success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'flash'))
)

assert driver.current_url != old_url, "Failed to update the url."

assert "You logged into a secure area!" in success_message.text

driver.quit()