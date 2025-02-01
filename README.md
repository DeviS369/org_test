# Selenium OrangeHRM Automation Framework

This project automates key functionalities of the OrangeHRM application using the Selenium WebDriver framework.

## Project Structure

selenium-orangehrm/ │ ├── │ ── config/ # Configuration files │ └── config.json # Application URL, credentials, and browser configurations │ ├── logs/ # Log files for tracking test execution │ └── test_execution.log │ ├── reports/ # Test reports (e.g., HTML or XML format) │ └── report.html │ ├── test_data/ # Test data files (e.g., JSON, CSV) │ └── login_test_data.json │ ├── tests/ # Test cases organized by module │ ├── init.py │ ├── test_login.py # Login test cases │ └── test_pim.py # PIM module test cases │ ├── pages/ # Page Object Model (POM) classes │ ├── init.py │ ├── login_page.py # Login page elements and actions │ └── pim_page.py # PIM page elements and actions │ ├── utils/ # Utility scripts (helpers, setup, teardown) │ ├── init.py │ ├── driver_setup.py # WebDriver setup and teardown │ ├── logger.py # Logging utility │ └── wait_utils.py # Explicit wait helpers │ ├── requirements.txt # Python dependencies └── README.md # Project documentation

## Prerequisites

- Python 3.8+
- Google Chrome (Ensure compatibility with the chromedriver version in `drivers/`)
- Pip (Python package manager)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/selenium-orangehrm.git
   cd selenium-orangehrm

## Run the tests
    python -m unittest discover -s tests

## Note : I have wrritten code for install chrome directly . So  drivers folder not neccessary for call chrome directly 
