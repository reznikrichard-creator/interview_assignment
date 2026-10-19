from tests.integration.steps import verify_search_limit


def test_search_parameter(search_api):
    response1 = search_api.search_books("The Hobbit", limit=3)
    response2 = search_api.search_books("The Hobbit", limit=5)

    verify_search_limit(response1, response2)