from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")
FIRST_PRODUCT = (By.CSS_SELECTOR, 'div[title*="Wired On-Ear Headphones"]')
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')]")
VIEW_CART_BTN = (By.XPATH, "//a[contains(@href,'/cart')]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(10)


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()

@when("Click on first product")
def open_first_product(context):
        context.driver.find_element(*FIRST_PRODUCT).click()
        sleep(4)
@when("Add product to cart")
def add_product_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(3)


@when("Click on view cart")
def click_on_view_cart(context):
    context.driver.find_element(*VIEW_CART_BTN).click()
    sleep(4)

@then('Verify at least 1 link shown')
def verify_1_header_link_shown(context):
    link = context.driver.find_element(*HEADER_LINKS)
    print(link)


@then('Verify {link_amount} links shown')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount) # "6" => int 6
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'

@then("Verify product is in the cart")
def verify_product_in_cart(context):
    sleep(3)
    cart_items = context.driver.find_elements(*CART_ITEM_TITLE)
    print(cart_items)
    assert any("heyday" in item.text.lower() for item in cart_items), \
        " Expected product not found in the cart."

@then("Verify product appears in cart")
def verify_product_in_cart(context):
    cart_items = context.driver.find_elements(*CART_ITEM_TITLE)
    assert any("heyday" in item.text.lower() for item in cart_items), \
        " Expected product not found in cart."
    print(" Product successfully found in cart.")