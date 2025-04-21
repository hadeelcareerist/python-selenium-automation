from features.steps.main_page_steps import SIDE_NAV_ADD_TO_CART_BTN
from selenium.webdriver.common.by import By
from time import sleep
from behave import then,when, given

SEARCH_RESULTS_TEXT = (By.CSS_SELECTOR, '[data-test="resultsHeading"]')
LISTINGS = (By.CSS_SELECTOR, '[data-test="product-card"]')
PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="product-title"]')
PRODUCT_IMG = (By.TAG_NAME, 'img')

@then('Click on the side nav Add to Cart button')
def click_side_nav_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(5)

@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    #assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
    context.app.search_results_page.verify_search_results(expected_text)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(2)
    # context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    products = context.driver.find_elements(*LISTINGS)[:8]  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)