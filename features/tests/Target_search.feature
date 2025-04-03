Feature: Target search test cases

  Scenario: user can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results show


  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on the cart icon
    Then verify "Your cart is empty" message is shown

  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    Then Verify Sign In form is opened


