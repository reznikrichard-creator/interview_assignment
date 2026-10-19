from tests.ui.steps import verify_5_results_render, search_for_books

def test_5_results_render(home):
    
    search_for_books(home, "The Hobbit")

    verify_5_results_render(home)