import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";
import { LoginPage } from "../../pages/LoginPage";

const loginPage = new LoginPage();

Given("I am on the OrangeHRM login page", () => {
  loginPage.visit();
  loginPage.usernameInput().should("be.visible");
  loginPage.passwordInput().should("be.visible");
});

Given("I am signed in with the configured demo account", () => {
  cy.login();
});

When("I submit the login form without credentials", () => {
  loginPage.submit();
});

When("I sign in with username {string} and an invalid password", (username: string) => {
  loginPage.usernameInput().clear().type(username);
  loginPage.passwordInput().clear().type("Incorrect-Password-123!", { log: false });
  loginPage.submit();
});

Then("required-field validation should be displayed on the login form", () => {
  cy.get(".oxd-input-field-error-message")
    .should("be.visible")
    .and("contain.text", "Required");
});

Then("an invalid-credentials message should be displayed", () => {
  cy.get(".oxd-alert-content-text")
    .should("be.visible")
    .and("contain.text", "Invalid credentials");
});

Then("I should remain on the login page", () => {
  cy.url().should("include", "/auth/login");
  loginPage.submitButton().should("be.visible");
});

Then("the dashboard should be displayed", () => {
  cy.url().should("include", "/dashboard/index");
  loginPage.assertDashboard();
});