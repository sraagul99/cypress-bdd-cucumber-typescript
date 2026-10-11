export class EmployeePage {
  visitAddEmployee(): this {
    cy.visit("/web/index.php/pim/addEmployee");
    return this;
  }

  visitEmployeeList(): this {
    cy.visit("/web/index.php/pim/viewEmployeeList");
    return this;
  }

  firstNameInput() {
    return cy.get('input[name="firstName"]');
  }

  lastNameInput() {
    return cy.get('input[name="lastName"]');
  }

  employeeIdInput() {
    return cy.contains(".oxd-input-group", "Employee Id").find("input");
  }

  saveButton() {
    return cy.contains('button[type="submit"]', "Save");
  }

  searchButton() {
    return cy.contains('button[type="submit"]', "Search");
  }
}