from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULTS_TEXT= (By.XPATH, "//div[@data-test= 'lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*= 'addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test= 'content-wrapper']h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test= 'content-wrapper'] [id*= 'addToCart']")



@given('Open target main page')
def open_target_main(context):
    #context.driver.get('https://www.target.com/') do instead
    context.app.main_page.open_main_page()
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_FIELD), message='Search field is not clickable')


@when('Search for {search_word}')
def search_product(context, search_word):
    #context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    #context.driver.find_element(*SEARCH_BTN).click()
    #search happens in the header
    context.app.header.search()
    sleep(8)


@when('Click on add to Cart button')
def click_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@when('store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('product name stored:', context.product_name)

@when("Confirm Add to Cart button from side navigation")
def side_nav_click_add_to_cart(context):
        context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
        sleep(5)



@then('Verify correct search result shown for {expected_result}')
def verify_search_results(context, expected_result):
 actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
 assert expected_result in actual_text, f'Error. Text{expected_result} not in {actual_text}'




