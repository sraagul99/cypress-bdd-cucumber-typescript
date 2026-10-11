Feature: Core OrangeHRM navigation
  As an authorized user
  I want to navigate between core modules
  So that I can access the relevant HR workflow

  @authenticated @smoke
  Scenario Outline: Open a core module from the main menu
    Given I am signed in with the configured demo account
    When I open the "<module>" module
    Then the URL should identify the "<route>" module
    And the application top bar should be visible

    Examples:
      | module      | route         |
      | PIM         | /pim/         |
      | Leave       | /leave/       |
      | Time        | /time/        |
      | Recruitment | /recruitment/ |
