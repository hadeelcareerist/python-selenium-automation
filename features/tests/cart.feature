
Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on the cart icon
    Then verify "Your cart is empty" message is shown




