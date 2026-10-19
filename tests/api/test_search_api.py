# GET /search.json?q=The%20Hobbit; assert HTTP 200, numFound number > 0, docs nonempty.


def test_search_hobbit(search_api):
    # Send GET request
    response = search_api.search_books("The Hobbit")

    # Verify HTTP status code
    assert response.status_code == 200

    # Convert JSON response into Python dictionary
    data = response.json()

    # Verify matching books exist
    assert data["numFound"] > 0

    # Verify returned documents are not empty
    assert len(data["docs"]) > 0
