from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")

link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "A/B Testing"))
)

link.click()

assert "/abtest" in driver.current_url, "Failed to navigate to A/B Testing page"

print("Successfully navigated to A/B Testing page.")

driver.quit()