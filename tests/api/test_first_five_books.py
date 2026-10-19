from tests.api.steps import verify_first_five_books


def test_first_five_books(search_api):
    query = "The Hobbit"

    response = search_api.search_books(query)

    verify_first_five_books(response, query)