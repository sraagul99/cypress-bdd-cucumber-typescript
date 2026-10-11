import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";
import { EmployeePage } from "../../pages/EmployeePage";

const employeePage = new EmployeePage();
let createdFirstName = "";
let createdLastName = "";

Given("I open the Add Employee form", () => {
  employeePage.visitAddEmployee();
  employeePage.firstNameInput().should("be.visible");
  employeePage.lastNameInput().should("be.visible");
});

When("I submit the employee form without required details", () => {
  employeePage.saveButton().click();
});

Then("required-field validation should be displayed on the employee form", () => {
  cy.get(".oxd-input-field-error-message")
    .should("have.length.at.least", 2)
    .and("contain.text", "Required");
});

When("I create an employee using unique portfolio test data", () => {
  cy.fixture("employee").then((employee) => {
    const unique = Date.now().toString().slice(-6);
    createdFirstName = `${employee.firstNamePrefix}${unique}`;
    createdLastName = `${employee.lastNamePrefix}${unique}`;
    const employeeId = `7${unique}`;

    employeePage.firstNameInput().clear().type(createdFirstName);
    employeePage.lastNameInput().clear().type(createdLastName);
    employeePage.employeeIdInput().clear().type(employeeId);
    employeePage.saveButton().click();
  });
});

Then("the employee details page should show the saved name", () => {
  cy.url().should("include", "/pim/viewPersonalDetails");
  cy.contains("h6", "Personal Details").should("be.visible");
  employeePage.firstNameInput().should("have.value", createdFirstName);
  employeePage.lastNameInput().should("have.value", createdLastName);
});

When("I open the Employee List page", () => {
  employeePage.visitEmployeeList();
});

Then("the Employee Information heading should be visible", () => {
  cy.contains("h5", "Employee Information").should("be.visible");
});

Then("the Search action should be visible", () => {
  employeePage.searchButton().should("be.visible");
});