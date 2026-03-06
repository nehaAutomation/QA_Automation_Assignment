# QA Automation Assignment
This repository contains the solution for the QA Engineer assignment.  
It includes API Automation, Pytest Test Suite, Postman Automation, and UI Automation using Playwright with Pytest.

# Project Structure
QA_Assignment
│
├── api_automation
│   ├── test_api_posts.py
│   └── first_five_posts.json
│
├── ui_tests
│   └── test_ui_playwright.py
│
├── requirements.txt
└── README.md


# Tech Stack Used
- Python
- Requests
- Pytest
- JSONSchema
- Postman
- Playwright

# Task 1: API Automation using Requests
Script performs the following actions using the public API:
https://jsonplaceholder.typicode.com/posts
### Validations performed
- Fetch all posts using GET request
- Validate response status code = **200**
- Verify each post contains required keys:
  - userId
  - id
  - title
  - body
- Save the **first 5 posts into a local JSON file**

Output file generated:
first_five_posts.json

# Task 2: Pytest API Test Suite
Pytest test suite covers the following validations:
### Response Time Validation
Ensures API response time is **less than 2 seconds**.
### Schema Validation
Each response is validated against the schema using **jsonschema**.
Required fields:
- userId
- id
- title
- body
### Parameterized Endpoint Testing
The following endpoints are tested:
- /posts
- /comments
- /users
All endpoints must return **status code 200**.


# Task 3: Postman Automation
Postman collection includes the following API tests:
### GET /posts
- Validate response status = **200**
### POST /posts
- Create a new post
- Validate response contains the same:
  - title
  - body
### DELETE /posts/{id}
- Validate response status **200 or 204**
Postman tests are written using **JavaScript test scripts**.

# Task 4: UI Automation using Playwright + Pytest
UI automation is performed on:
https://rahulshettyacademy.com/AutomationPractice/
### Automated Test Scenarios
- Radio Button selection
- Checkbox validation
- Dropdown selection
- Switch Tab functionality
Playwright is used with **pytest-playwright** for test execution.

# Task 5: QA Based Questions
Two scenario-based questions were provided to evaluate QA leadership, problem-solving, and process improvement approach.
1.Sprint velocity is dropping due to flaky automation tests while leading a QA team of 4 engineers.
2.Two critical bugs were reported by the client during production release which were missed in QA.

Detailed answers explaining the **approach to identify root causes, stabilize automation tests, and improve QA processes** are documented in:
***QA_qnA.md***

# Setup Instructions
1 Install dependencies
bash
pip install -r requirements.txt