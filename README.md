# QA Automation Assignment

## Project Overview

This project demonstrates an automation framework for **API and UI testing** using Python.
It includes automated validation of REST APIs, UI testing using Playwright, logging, and HTML reporting.

The framework is designed using **best practices such as Page Object Model (POM), pytest fixtures, configuration management, and modular structure.**

---

# Tech Stack

* Python
* pytest
* Playwright
* requests
* pytest-html
* logging

---

# Project Structure

```
QA_Assignment
│
├── api
│   ├── api_client.py
│   └── test_posts_api.py
│
├── api_automation
│   └── fetch_posts.py
│
├── data
│   └── first_five_posts.json
│
├── postman_collection
│   └── QA_Assignment.postman_collection.json
│
├── ui
│   ├── pages
│   │   └── practice_page.py
│   └── tests
│       ├── conftest.py
│       └── test_ui_playwright.py
│
├── utils
│   ├── config.py
│   └── logger.py
│
├── logs
│   └── test.log
│
├── reports
│   └── report.html
│
├── pytest.ini
└── README.md
```

---

# Features Implemented

### API Automation

* GET request validation using **requests**
* Response schema validation
* Status code verification
* Data extraction and storage
* API tests implemented using **pytest**

### UI Automation

* Implemented using **Playwright**
* Page Object Model (POM)
* Automated tests for:

  * Page title validation
  * Radio buttons
  * Checkboxes
  * Dropdown selection
  * New tab navigation

### Logging

* Centralized logging using Python **logging module**
* Logs stored in `logs/test.log`

### Test Reporting

* HTML reports generated using **pytest-html**
* Reports stored in `reports/report.html`

---

# Setup Instructions

## 1. Clone the Repository

```
git clone https://github.com/<your-username>/QA_Assignment.git
cd QA_Assignment
```

---

## 2. Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate
```

For Windows:

```
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

Install Playwright browsers:

```
playwright install
```

---

# Running Tests

Run all tests:

```
pytest
```

Run only API tests:

```
pytest api
```

Run only UI tests:

```
pytest ui
```

---

# Generate HTML Report

```
pytest --html=reports/report.html --self-contained-html
```

Open report:

```
reports/report.html
```

---

# API Script

The script `fetch_posts.py` fetches posts from the API and saves the **first five posts** into a JSON file.

Run:

```
python api_automation/fetch_posts.py
```

Output file:

```
data/first_five_posts.json
```

---

# API Endpoint Used

https://jsonplaceholder.typicode.com/posts

---

# UI Test Website

https://rahulshettyacademy.com/AutomationPractice/

---

# Postman Collection

A Postman collection is included in:

```
postman_collection/QA_Assignment.postman_collection.json
```

---

# Author

Neha Chorge
QA Automation Engineer
