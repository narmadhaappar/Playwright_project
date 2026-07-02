# Playwright_project

PLAYWRIGHT_PROJECT/
│
├── features/ 
     └── api.feature
     └── ui.feature               # Feature files (BDD scenarios in Gherkin)
│
├── Pages/                  # Page Object Models
│   └── HomePage.py         # Example page class
│
├── step_defs/              # Step definitions linking Gherkin steps to code
│   ├── api_steps.py
│   └── ui_steps.py
│
├── utils/  
|   ├── api_utils.py
│   └── common_utils.py  
|   ├── config.py
│   └── data_generator.py              # Utility functions (helpers, configs, constants)
│
├── verification/           # Custom assertions & validation logic
│
├── videos/                 # Test execution recordings (Playwright videos)
│
├── conftest.py             # Pytest configuration & fixtures
├── package-lock.json       # Dependency lock file
└── README.md               # Project documentation


Test Coverage
UI Test
-HomePage Validations
-Category Navigation
-Search Functionality

API Test
-create Operation
-Retrieve Operation
-Post Operation
-Delete Operations

Features
-POM
-API service layer
-Data generator for API payload
-Screenshot capture
-Logging

##Running UI Test
 pytest step_defs/ui_steps.py -v

##Running API Test
 pytest step_defs/api_steps.py -v




