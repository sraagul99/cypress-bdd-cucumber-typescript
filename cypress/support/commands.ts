import { LoginPage } from "../pages/LoginPage";

Cypress.Commands.add("login", (username?: string, password?: string) => {
  const resolvedUsername = username ?? Cypress.env("username");
  const resolvedPassword = password ?? Cypress.env("password");

  if (!resolvedUsername || !resolvedPassword) {
    throw new Error(
      "Credentials are not configured. Set CYPRESS_ORANGEHRM_USERNAME and CYPRESS_ORANGEHRM_PASSWORD."
    );
  }

  const loginPage = new LoginPage();
  loginPage.visit();
  loginPage.login(resolvedUsername, resolvedPassword);
  loginPage.assertDashboard();
});

declare global {
  namespace Cypress {
    interface Chainable {
      /** Log in with explicit or environment-configured demo credentials. */
      login(username?: string, password?: string): Chainable<void>;
    }
  }
}

export {};