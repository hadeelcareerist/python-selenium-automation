from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

    @then('Verify user can click through colors')
    def click_and_verify_colors(context):
        # ✅ Updated for product A-91511634
        expected_colors = ['Gray', 'Ivory', 'Light Blue', 'Sage']
        actual_colors = []

        colors = context.driver.find_elements(*COLOR_OPTIONS)

        for color in colors:
            color.click()
            sleep(1)

            selected_color = context.driver.find_element(*SELECTED_COLOR).text
            print('Current color', selected_color)

            selected_color = selected_color.split('\n')[1]
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
