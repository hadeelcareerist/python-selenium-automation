from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')
    sleep(6)

@then('should see at least 10 benefit cells')
def verify_benefit_cells(context):
 elements = context.driver.find_element(By.CSS_SELECTOR, "[class*='storycard--text']")
 assert len(elements) >= 10, f"Expected at least 10 benefit cells, got {len(elements)}"


