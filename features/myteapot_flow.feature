Feature: My Lovely Teapot service flow

  # Background: Ensuring that all dependencies are up and running
  #   Given Knowledge Service is up and running


  Scenario: Accessing documentation
    Given a user with "valid" credentials
    When the user gets documentation
    Then the response status should be "200"
    And the response should contain the documentation content

  Scenario: Create IcM ticket with valid data
    Given a user with "valid" credentials
    And "valid" IcM ticket data
    When the user creates IcM ticket
    Then the response status should be "201"
    And the response should contain valid IcM ticket ID
    And the response should contain user Knowledge

  Scenario: Create IcM ticket with invalid data
    Given a user with "valid" credentials
    And "invalid" IcM ticket data
    When the user creates IcM ticket
    Then the response status should be "400"