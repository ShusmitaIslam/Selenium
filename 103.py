from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Form Authentication"))
)

old_url = driver.current_url

link.click()

new_page_title = WebDriverWait(driver, 10).until(
    lambda d: d.current_url != old_url
)

print(driver.title)
print(driver.current_url)

driver.quit()
