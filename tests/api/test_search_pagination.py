from tests.api.steps import verify_pagination


def test_search_pagination(search_api):
    response1 = search_api.search_books("The Hobbit", page=1, limit=5)
    response2 = search_api.search_books("The Hobbit", page=2, limit=5)

    verify_pagination(response1, response2, limit=5)