Feature: PIM employee management
  As an authorized HR user
  I want to manage employee records
  So that employee information is recorded accurately

  @authenticated @smoke
  Scenario: Add Employee form enforces required fields
    Given I am signed in with the configured demo account
    And I open the Add Employee form
    When I submit the employee form without required details
    Then required-field validation should be displayed on the employee form

  @authenticated @regression
  Scenario: Create an employee and verify the saved details
    Given I am signed in with the configured demo account
    And I open the Add Employee form
    When I create an employee using unique portfolio test data
    Then the employee details page should show the saved name

  @authenticated @smoke
  Scenario: Employee list is available
    Given I am signed in with the configured demo account
    When I open the Employee List page
    Then the Employee Information heading should be visible
    And the Search action should be visible
