'''''''''''''''''''Open Library — UI, API & Integration Test Automation Framework'''''''''''''''''''

# Create virtual environment
python3 -m venv .venv

# Activate environment (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser
python -m playwright install chromium

# Run all tests
python -m pytest -v

# Run API tests
python -m pytest tests/api/ -v

# Run UI tests
python -m pytest tests/ui/ -v

# Run integration tests
python -m pytest tests/integration/ -v


Integration Testing — Catalog and Ranking Variability

The integration test compares normalized book titles from the Open Library API and UI for the search term "The Hobbit".

The test checks up to 5 API results against the first 5 UI results, ignoring capitalization and surrounding whitespace.

Open Library's search rankings and catalog may change over time, so results may appear in different orders or contain different editions. The test therefore verifies that at least one title matches without requiring identical result positions.

A failed match may indicate ranking or catalog differences rather than a functional defect.