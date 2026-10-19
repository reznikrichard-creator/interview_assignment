# Test is blocked due to human verification requirment after clicking on first result




# from tests.ui.steps import search_for_books, save_results
# def test_book_details(page, home, product_details):
#     # 1. Search for The Hobbit
#     search_for_books(home, "The Hobbit")

#     # 2. Save search result information
#     search_title, search_author = save_results(home)

#     # 3. Click the first result
#     home.search_rows.first.click()

#     if page.get_by_role("button", name="Verify you are human").is_visible():
#         print("Human verification required")
#         page.pause()

#     # 4. Verify details page title
#     product_details.hobbit_title.wait_for(state="visible")
#     details_title = product_details.hobbit_title.inner_text().strip()

#     assert search_title == details_title


