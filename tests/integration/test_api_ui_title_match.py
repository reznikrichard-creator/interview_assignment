
from tests.integration.steps import verify_api_title_in_ui
from tests.ui.steps import search_for_books

# documented catalog/rank variability in readme.md

def test_api_ui_title_match(search_api, home):


    # 1. Search using the API
    response = search_api.search_books("The Hobbit", limit=5)

    api_books = response.json()["docs"]


    # 2. Collect the first 5 API titles
    api_titles = [
        book["title"]
        for book in api_books[:5]
        if book.get("title")
    ]

    # 3. Search using the UI
    search_for_books(home, "The Hobbit")
    home.search_rows.first.wait_for(state="visible")

    # 4. Collect up to 5 UI titles
    ui_titles = []

    for i in range(min(home.search_rows.count(), 5)):
        title = home.title.nth(i).inner_text()
        ui_titles.append(title)

    # 5. Compare normalized API and UI titles
    verify_api_title_in_ui(api_titles, ui_titles)
