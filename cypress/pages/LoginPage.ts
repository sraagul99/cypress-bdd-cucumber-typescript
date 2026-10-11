export class LoginPage {
  visit(): this {
    cy.visit("/web/index.php/auth/login");
    return this;
  }

  usernameInput() {
    return cy.get('input[name="username"]');
  }

  passwordInput() {
    return cy.get('input[name="password"]');
  }

  submitButton() {
    return cy.get('button[type="submit"]');
  }

  submit(): this {
    this.submitButton().should("be.enabled").click();
    return this;
  }

  login(username: string, password: string): this {
    this.usernameInput().should("be.visible").clear().type(username);
    this.passwordInput().should("be.visible").clear().type(password, { log: false });
    this.submit();
    return this;
  }

  assertDashboard(): this {
    cy.get(".oxd-topbar-header-breadcrumb-module")
      .should("be.visible")
      .and("contain.text", "Dashboard");
    return this;
  }
}