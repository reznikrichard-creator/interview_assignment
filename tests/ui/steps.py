def verify_home_page(self):
    assert self.page.title() == "Welcome to Open Library | Open Library"

def search_for_books(home, title: str):
    home.search_icon()
    home.enter_search(title)
    
    home.search_rows.nth(4).wait_for(state="visible")

def verify_5_results_render(home):
    count = home.search_rows.count()
    assert count >= 5, f"Expected at least 5 results, found {count}"

def verify_title_and_author(home):
    for i in range(5):
        title = home.title.nth(i)

        assert title.is_visible()
        assert title.inner_text().strip()

        author = home.search_rows.nth(i).locator(".result__author")

        if author.count() > 0:
            assert author.inner_text().strip()

def save_results(home):
    
    # 1. Save the first result's title and author
    first_result = home.search_rows.first

    # 2. Save its title
    book_title = first_result.locator(".result__title").inner_text().strip()

    # 3. Save its author, if present
    book_author = first_result.locator(".result__author")

    if book_author.count() > 0:
        author_name = book_author.inner_text().strip()
    else:
        author_name = None
    
    return book_title, author_name

    