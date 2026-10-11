import "dotenv/config";
import { defineConfig } from "cypress";
import createBundler from "@bahmutov/cypress-esbuild-preprocessor";
import { addCucumberPreprocessorPlugin } from "@badeball/cypress-cucumber-preprocessor";
import { createEsbuildPlugin } from "@badeball/cypress-cucumber-preprocessor/esbuild";

export default defineConfig({
  video: true,
  screenshotOnRunFailure: true,
  e2e: {
    baseUrl: process.env.CYPRESS_BASE_URL ?? "https://opensource-demo.orangehrmlive.com",
    specPattern: "cypress/e2e/features/**/*.feature",
    supportFile: "cypress/support/e2e.ts",
    defaultCommandTimeout: 10000,
    pageLoadTimeout: 60000,
    viewportWidth: 1440,
    viewportHeight: 900,
    retries: { runMode: 1, openMode: 0 },
    async setupNodeEvents(on, config) {
      await addCucumberPreprocessorPlugin(on, config);

      on("file:preprocessor", createBundler({
        plugins: [createEsbuildPlugin(config)],
      }));

      config.env.username =
        process.env.CYPRESS_ORANGEHRM_USERNAME ?? config.env.username;
      config.env.password =
        process.env.CYPRESS_ORANGEHRM_PASSWORD ?? config.env.password;

      return config;
    },
  },
});