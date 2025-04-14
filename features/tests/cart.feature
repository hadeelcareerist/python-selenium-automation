
Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on the cart icon
    Then verify "Your cart is empty" message is shown

Feature: Cart operations
  Scenario: Add a product to the cart and verify it will appears
    Given Open target main page
    When Search for headphones
    When Click on first product
    When Add product to cart
    When Click on view cart
    Then Verify product appears in cart


