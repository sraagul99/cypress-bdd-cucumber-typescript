import { When, Then } from "@badeball/cypress-cucumber-preprocessor";

When("I open the {string} module", (moduleName: string) => {
  cy.contains(".oxd-main-menu-item", moduleName).should("be.visible").click();
});

Then("the URL should identify the {string} module", (route: string) => {
  cy.url().should("include", route);
});

Then("the application top bar should be visible", () => {
  cy.get(".oxd-topbar-header").should("be.visible");
});