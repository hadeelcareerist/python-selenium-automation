Feature: Target search test cases

  Scenario: User can search for a product on Target
#  Scenario: User can search for a tea on Target
#    Given Open target main page
#    When Search for tea
#    Then Verify correct search results shown for tea
#
#  Scenario: User can search for a iPhone on Target
#    Given Open target main page
#    When Search for iPhone
#    Then Verify correct search results shown for iPhone
#
#  Scenario: User can search for a dress on Target
#    Given Open target main page
#    When Search for dress
#    Then Verify correct search results shown for dress

  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results show
    When Search for <search_word>
    Then Verify correct search results shown for <expected_text>
    Examples:
    |search_word  |expected_text  |
    |tea          |tea            |
    |iPhone       |iPhone         |
    |dress        |dress          |
