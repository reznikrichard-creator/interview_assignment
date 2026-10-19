def normalize_title(title):
    title = title.lower().strip()
    return title


def verify_api_title_in_ui(api_titles, ui_titles):
    # Normalize both lists of titles
    normalized_api = [normalize_title(title) for title in api_titles]
    normalized_ui = [normalize_title(title) for title in ui_titles]

    match_found = False

    for title in normalized_api:
        if title in normalized_ui:
            match_found = True
            break

    assert match_found


def verify_search_limit(response1, response2):
    assert response1.status_code == 200
    assert response2.status_code == 200

    # Convert each HTTP response into a Python dictionary using .json()
    # ["docs"] accesses the list of books returned by Open Library

    books1 = response1.json()["docs"]
    books2 = response2.json()["docs"]

    assert len(books1) == 3
    assert len(books2) == 5