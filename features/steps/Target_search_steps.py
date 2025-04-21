from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

WAIT_TIME = 10

@given('Open Target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located(By.ID, 'search'))

@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)

@when('click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[contains(@aria-label,'cart')]").click()
    sleep(5)


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(3)

@when('Click Sign In from right-side navigation menu')
def click_sign_in_nav(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/signin')]").click()
    sleep(3)


@then('Verify Sign In form is opened')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Sign into your Target account')]").text
    expected_text = "Sign into your Target account"

    assert expected_text == actual_text, f"Error: Expected '{expected_text}', but found '{actual_text}'"
@then('Verify correct search results shown for tea')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    expected_text = 'tea'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

