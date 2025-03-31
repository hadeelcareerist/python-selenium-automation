from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# Open the Target website
driver.get("https://www.target.com/")
print("Target homepage opened.")

# 1. Click the 'Sign In' button in the header
sign_in_button_home = driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']")
sign_in_button_home.click()
print("Clicked on Sign In button on homepage.")

# 2. Wait longer for the side navigation to open
sleep(5)  # Wait to allow side navigation to load

# 3. Try Different Locator Options
try:
    # Option 1: Using exact text
    side_sign_in_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]")
except:
    try:
        # Option 2: Using partial link text
        side_sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
    except:
        try:
            # Option 3: Using parent-child relationship (most reliable)
            side_sign_in_link = driver.find_element(By.XPATH, "//div[contains(@class, 'styles__StyledAccountNav')]//a[contains(text(), 'Sign in')]")
        except Exception as e:
            print("Sign In link not found. Error:", e)
            driver.quit()
            exit()

# 4. Click the 'Sign In' link from side navigation
side_sign_in_link.click()
print("Clicked on 'Sign In' link from side navigation.")

# 5. Verify that the SignIn page is loaded by checking for the text
sleep(2)
try:
    sign_in_text = driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
    print('Sign into your Target account text is visible:', sign_in_text.is_displayed())
except:
    print("Text 'Sign into your Target account' not found.")

# 6. Verify the Sign In button
try:
    sign_in_button = driver.find_element(By.XPATH, "//button[@data-test='LoginForm__submitButton']")
    print("Sign In button is visible:", sign_in_button.is_displayed())
except:
    print("Sign In button not found.")

# 7. Close the browser
driver.quit()
