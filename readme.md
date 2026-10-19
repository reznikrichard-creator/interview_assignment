# Open Library — UI, API & Integration Test Automation Framework

Automated testing framework for [Open Library](https://openlibrary.org), built with **Python, pytest, Playwright, and Requests**.

The project validates book search functionality across the user interface and REST API, including search results, book details, pagination, and consistency between API and UI data.

Tests can be executed locally or through **GitHub Actions**.

## Technology Stack

- **Python** — Test automation language
- **pytest** — Test execution, fixtures, and assertions
- **Playwright** — Browser automation and UI testing
- **Requests** — REST API testing
- **Page Object Model (POM)** — Reusable UI interactions and locators
- **GitHub Actions** — Continuous integration
- **pytest-html** — HTML test reporting

## Project Structure

```text
openlibrary-test-automation/
├── .github/
│   └── workflows/
├── api/
│   └── SearchAPI.py
├── pages/
│   ├── HomePage.py
│   └── ProductDetails.py
├── tests/
│   ├── api/
│   ├── ui/
│   └── integration/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── readme.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/reznikrichard-creator/openlibrary-test-automation.git
cd openlibrary-test-automation
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Install Playwright Chromium

```bash
python -m playwright install chromium
```

## Running Tests

### Run all tests

```bash
python -m pytest -v
```

### Run API tests

```bash
python -m pytest tests/api/ -v
```

### Run UI tests

```bash
python -m pytest tests/ui/ -v
```

### Run integration tests

```bash
python -m pytest tests/integration/ -v
```

### Run UI tests with a visible browser

```bash
python -m pytest tests/ui/ -v --headed
```

### Display print statements during execution

```bash
python -m pytest -v -s
```

## Test Coverage

### API Testing

Validates Open Library's book search API.

- Successful searches and HTTP response status
- Search result structure and required fields
- Empty results for nonexistent search terms
- Pagination and result limits
- Unique book identifiers across paginated results

### UI Testing

Validates book search functionality through the browser.

- Search for books using a fixed search term
- Verify at least five results are displayed
- Validate book titles and authors when available
- Open a book's details page
- Verify book details against the selected search result
- Navigate back to search results

### Integration Testing

Validates consistency between the Open Library API and UI.

- Search for *The Hobbit* using both interfaces
- Retrieve API and UI book titles
- Normalize titles for comparison
- Verify title consistency according to the implemented matching rules
- Validate API result-limit behavior

## Integration Testing — Catalog and Ranking Variability

Open Library's search results may vary because of changes in catalog data, book editions, and search ranking.

The framework compares normalized book titles returned by the API and displayed in the UI.

Differences in capitalization, formatting, or edition descriptions may require additional normalization.

Because Open Library is a live public service, some differences may reflect catalog or ranking changes rather than application defects.

**Note:** The exact matching requirement depends on the current implementation of `verify_api_title_in_ui()`.

## Continuous Integration

GitHub Actions automatically executes the test framework on pushes and pull requests. The workflow can also be started manually.

The workflow includes three test jobs:

- API Tests
- UI Tests
- Integration Tests

UI and integration tests use Playwright Chromium in headless mode.

## Test Reports and Debugging

Generate an HTML report:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

For Playwright screenshots and traces on failure:

```bash
python -m pytest tests/ui/ -v --screenshot only-on-failure --tracing retain-on-failure
```

GitHub Actions uploads test reports and available failure artifacts for review.

## Assumptions and Limitations

- Tests use the public Open Library website and API.
- An internet connection is required for live API and UI tests.
- Search rankings and catalog records can change over time.
- Temporary network failures, rate limiting, or human-verification challenges may affect test execution.
- Tests do not require authentication credentials for the covered public search functionality.
- Integration comparisons use normalization rules to account for documented title variations.

## Repository

[Open Library Test Automation — GitHub](https://github.com/reznikrichard-creator/openlibrary-test-automation)