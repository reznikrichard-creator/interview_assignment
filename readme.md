FrameWork Dependencies

Dependency	Purpose
pytest	Test runner and assertions
pytest-playwright	Browser automation fixtures
pytest-html	HTML test reports
pytest-xdist	Parallel test execution
playwright	Browser automation engine, installed through pytest-playwright



Integration Testing — Catalog and Ranking Variability

The integration test compares normalized book titles from the Open Library API and UI for the search term "The Hobbit".

The test checks up to 5 API results against the first 5 UI results, ignoring capitalization and surrounding whitespace.

Open Library's search rankings and catalog may change over time, so results may appear in different orders or contain different editions. The test therefore verifies that at least one title matches without requiring identical result positions.

A failed match may indicate ranking or catalog differences rather than a functional defect.