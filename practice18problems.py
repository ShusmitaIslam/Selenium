from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

#step-1-browser open
driver = webdriver.Chrome()
driver.get('https://automationexercise.com/')
driver.maximize_window()
time.sleep(5)

#step-2-homepage loading
if "automationexercise" in driver.current_url:
    print("Homepage Loaded")
else:
    print("Homepage is not loading")

#step-3-Click "Signup / Login"
signup_click = driver.find_element(By.CSS_SELECTOR, ".navbar-nav > li:nth-child(4) > a:nth-child(1)")
signup_click.click()
time.sleep(2)

#step-4-Verify "New User Signup!" section visible
signup_visible = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/h2")
if signup_visible.is_displayed():
    print("'New User Signup!' section is visible")
else:
    print("'New User Signup!' section is not visible")
    
#step-5-Fill Name
signup_name = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
signup_name.send_keys("Shusmita")

#step-6-Fill Email
signup_email = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
signup_email.send_keys("shusmitashoron1@gmail.com")
time.sleep(2)

#step-7-Click Signup button
for_signup = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button')
for_signup.click()
time.sleep(2)

#step-8-Wait until Account Information page appears
acc_info = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form"]/div/div/div/div/h2/b')))
print("Account information page is visible.")

#step-9-Select Radio Button
title_gender1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'id_gender1')))
title_gender1.click()

if title_gender1.is_selected():
    print("Mr. is selected")
    
title_gender2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'id_gender2')))
title_gender2.click()

if title_gender2.is_selected():
    print("Mrs. is selected")
    
time.sleep(2)

#step-10-Password field fill
password = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'password')))
password.send_keys("12345")

#step-11-Date Dropdown
#Day
day = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'days')))
day_dropdown = Select(day)
day_dropdown.select_by_visible_text("10")
if day_dropdown.first_selected_option.text == "10":
    print("Day selected successfully")
    
#Month
month = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'months')))
month_dropdown = Select(month)
month_dropdown.select_by_visible_text("January")
if month_dropdown.first_selected_option.text == "January":
    print("Month selected successfully")

#Year
year = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'years')))
year_dropdown = Select(year)
year_dropdown.select_by_visible_text("2020")
if year_dropdown.first_selected_option.text == "2020":
    print("Year selected successfully")
time.sleep(2)

#step-12-Newsletter Checkbox
newsletter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'newsletter')))
newsletter.click()
if newsletter.is_selected():
    print("Newsletter checkbox is successfully selected")
    
#step-13-Special Offers Checkbox
special_offer = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'optin')))
special_offer.click()
if special_offer.is_selected():
    print("Special offer checkbox is successfully selected")
    
#step-14-Fill:First Name, Last Name, Company, Address
first_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'first_name')))
first_name.send_keys("Shusmita")

last_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'last_name')))
last_name.send_keys("Islam")

company = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'company')))
company.send_keys("WYZE TECH LTD")

address1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'address1')))
address1.send_keys("Lotus Kamal Tower")

address2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'address2')))
address2.send_keys("Gulshan-1")

#step-15-Country Dropdown
country = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'country')))
country_dropdown = Select(country)
country_dropdown.select_by_visible_text("India")
if country_dropdown.first_selected_option.text == "India":
    print("Country is selected successfully")

#step-16-Fill:State, City, Zip Code, Mobile Number
state = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "state")))
state.send_keys("Bangladesh")

city = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "city")))
city.send_keys("Dhaka")

zip_code = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "zipcode")))
zip_code.send_keys("1215")

mobile_number = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mobile_number")))
mobile_number.send_keys("01557678258")

time.sleep(2)

#step-17-Click Create Account
create_account = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form"]/div/div/div/div/form/button')))
create_account.click()

#step-18-Verify Success Message
account_created = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form"]/div/div/div/h2/b')))
actual_text = account_created.text
expected_text = "ACCOUNT CREATED!"
if actual_text.upper() == expected_text:
    print("Success message verified")
else:
    print("Verification failed")









    
