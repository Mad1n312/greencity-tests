**This project contains test cases and a suite of automated tests for the "Events" section of the GreenCity website.**
**Link to testing page:** [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events)

**Author: Щербан Данило**

## Tech Stack

- Python 3.10+
- Selenium 4
- Pytest

## Project Structure

```text
.
|-- components/
|   |-- base_component.py
|   `-- event_card_components.py
|-- pages/
|   |-- base_page.py
|   `-- events_page.py
|-- tests/
|   |-- test_01_search_event.py
|   |-- test_02_filter_by_status.py
|   `-- test_04_guest_redirection_to_login.py
|--.gitignore
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
`-- README.md
```

## Test Design

- `pages/` contains page objects (screen-level behavior).
- `components/` contains reusable UI components (modal, cards, etc.).
- `tests/` contains Pytest test cases.
- `tests/conftest.py` provides the `init_driver` fixture for WebDriver setup/teardown.

## Prerequisites

1. Python 3.10 or newer installed.
2. Google Chrome installed.
3. ChromeDriver compatible with your Chrome version (or Selenium Manager available in your environment).

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test module:

```bash
pytest tests/test_01_search_event.py
```

Run a single test case:

```bash
pytest tests/test_01_search_event.py::test_tc01_search_by_name
```


## Allure Reporting (Optional)

This repository name suggests Allure usage, but `allure-pytest` is not currently pinned in `requirements.txt`.

Install plugin:

```bash
pip install allure-pytest
```

Generate results during test run:

```bash
pytest --alluredir=allure-results
```

Serve report (requires Allure CLI installed on your machine):

```bash
allure serve allure-results
```

## Current Test Coverage

- Header language switch (`uk`/`en`) and UI text checks.
- Search by name and validation of results 
- Filtering by status (Open/Closed)
- Guest redirect to Login



