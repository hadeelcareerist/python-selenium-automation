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
# find elements by id
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-search-submit-button')

#find element by xpath
driver.find_element(By.XPATH, "//input[@placeholder= 'search amazon']")
driver.find_element(By.XPATH, "//input[@role= 'searchbox']")

#by xpath any tag but with attribute = value

driver.find_element(By.XPATH, "//*[@role= 'searchbox']")

#by xpath multiple attributes

driver.find_element(By.XPATH, "//input[@tabindex= '0' and @name='field-keywords']")

#BY Xpath text()
driver.find_element(By.XPATH, "//a[text()= 'Best Sellers']")

#by xpath text() + attribute
driver.find_element(By.XPATH, "//a[text()= 'Best Sellers' and@class='nav-a ']")

#by xpath partial match
driver.find_element(By.XPATH, "//select[contains(@aria-describedby, 'search')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Best Seller') and @class='nav-a ']")

