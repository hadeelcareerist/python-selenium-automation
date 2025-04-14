from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(2)

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
@then('Verify correct search results show')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    expected_text = 'tea'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

    @then('verify "Your cart is empty" message is shown')
    def verify_empty_cart_message(context):
        actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Your cart is empty')]").text
        expected_result = "Your cart is empty"
        assert expected_result in actual_result, f"Error. Text '{expected_result}' not found in '{actual_result}'"