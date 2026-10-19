def verify_first_five_books(response, query):
    assert response.status_code == 200

    docs = response.json()["docs"]

    # Verify at least 5 books were returned
    assert len(docs) >= 5

    for book in docs[:5]:
        # Verify title is in results and is not empty
        assert query.lower() in book["title"].lower()

        # Verify author_name only if present
        if "author_name" in book:
            assert isinstance(book["author_name"], list)

            for author in book["author_name"]:
                assert isinstance(author, str)
                assert author.strip() != ""


def verify_empty_search(response):
    assert response.status_code == 200

    data = response.json()

    assert data["numFound"] == 0
    assert data["docs"] == []


def verify_pagination(response1, response2, limit):
    # 1. Verify both API requests were successful
    assert response1.status_code == 200
    assert response2.status_code == 200

    # 2. Get the list of books from each page
    page1 = response1.json()["docs"]
    page2 = response2.json()["docs"]

    # 3. Verify neither page exceeds the requested limit
    assert len(page1) <= limit
    assert len(page2) <= limit

    # 4. Get the book IDs from each page
    # Only include books that have a "key"
    keys1 = []
    keys2 = []

    for book in page1:
        if "key" in book:
            keys1.append(book["key"])

    for book in page2:
        if "key" in book:
            keys2.append(book["key"])

    # 5. Verify no book from page 1 appears on page 2
    for key in keys1:
        assert key not in keys2, f"Duplicate book found: {key}"
