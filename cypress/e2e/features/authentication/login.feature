Feature: OrangeHRM authentication
  As an application user
  I want clear feedback when I sign in
  So that I understand whether I can access the application

  @smoke @negative
  Scenario: Required-field validation for an empty login form
    Given I am on the OrangeHRM login page
    When I submit the login form without credentials
    Then required-field validation should be displayed on the login form
    And I should remain on the login page

  @smoke @negative
  Scenario: Invalid credentials are rejected
    Given I am on the OrangeHRM login page
    When I sign in with username "invalid.portfolio.user" and an invalid password
    Then an invalid-credentials message should be displayed
    And I should remain on the login page

  @authenticated @smoke
  Scenario: Authorized user can access the dashboard
    Given I am signed in with the configured demo account
    Then the dashboard should be displayed
