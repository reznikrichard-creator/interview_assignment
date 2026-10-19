from tests.ui.steps import search_for_books, verify_title_and_author


def test_title_author(home):
    
    search_for_books(home, "The Hobbit")

    verify_title_and_author(home)