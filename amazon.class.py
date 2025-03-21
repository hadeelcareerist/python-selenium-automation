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

#open the url
driver.get('https://www.amazon.com')

#by ID
driver.element(By.ID,'twotabsearchtextbox' )

#by Xpath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@role = 'searchbox']")

#by xpath , multiple
driver.find_element(By.XPATH, "//input[@tabindex = '0' and @name= 'field-keywords']")

#by xpath any tag
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")

#by xpath using text
driver.find_element(By.XPATH, "//a[text()= 'Best Sellers']")

#by xpath using text and attribute
driver.find_element(By.XPATH, "//a[text()= 'Best Sellers' and @class='nav-a  ']")

#by xpath contains function
driver.find_elemet(By.XPATH, "//h2[contains(text(), 'Luxury')]")

#by partial attribute match
driver.find_element(By.XPATH, "//select(contains(@class, 'nav-search-dropdown')]")

