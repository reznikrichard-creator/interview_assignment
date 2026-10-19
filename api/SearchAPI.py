import requests


class SearchAPI:
    def __init__(self):
        self.base_url = "https://openlibrary.org"

    def search_books(self, query, page=1, limit=5):
        params = {
            "q": query,
            "page": page,
            "limit": limit
        }

        return requests.get(
            f"{self.base_url}/search.json",
            params=params,
            timeout=15,
        )