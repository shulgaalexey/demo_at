Feature: User Sign-In API

  Scenario: Valid user sign-in
    Given a user with "valid" credentials
    When the user sends signin request
    Then the response status should be "200"
    And the response should contain a valid JWT token

  Scenario: Invalid user sign-in
    Given a user with "invalid" credentials
    When the user sends signin request
    Then the response status should be "401"
