from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=3ZAPFSJ47Y6F2PYH83JS&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

sleep(15)
#Amazon Logo
driver.find_element(By.CSS_SELECTOR, "[class='a-icon a-icon-logo']")

#Create Account Heading
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#First Name field
driver.find_element(By.ID, 'ap_customer_name')

#Email Field
driver.find_element(By.ID, 'ap_email')

#Password Field
driver.find_element(By.CSS_SELECTOR, "input#ap_password")

#Re-enter Pass
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

#hint Pass
driver.find_element(By.CSS_SELECTOR, "div.a-alert-content")

#continue button or create your amazon account
driver.find_element(By.CSS_SELECTOR, "[aria-labelledby='auth-continue-announce']")
sleep(5)

#condition of use
driver.find_element(By.CSS_SELECTOR, "a[href*='condition']")
sleep(5)

#Privacy Note
driver.find_element(By.CSS_SELECTOR, "a[href*='privacy']")
sleep(5)

#sign in
driver.find_element(By.CSS_SELECTOR, "a[class='a-link-emphasis']")





