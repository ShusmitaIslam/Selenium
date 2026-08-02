# Problem 6: Count All Links

# Website:
# https://the-internet.herokuapp.com/

# Task
# Browser ওপেন করো।
# Website-এ যাও।
# Page-এর সব <a> tag খুঁজে বের করো।
# মোট কতগুলো link আছে, print করো।
# প্রথম ১০টি link-এর text print করো।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

links = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
)


print(len(links))

for link in links[:10]:
    print(link.text)

