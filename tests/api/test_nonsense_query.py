from tests.api.steps import verify_empty_search


def test_nonsense_query(search_api):
    response = search_api.search_books("zzzxqv987654321nomatch")

    verify_empty_search(response)