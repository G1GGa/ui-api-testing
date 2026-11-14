from pages.login_page import LoginPage

def test_valid_user_login(page):
    login_page = LoginPage(page)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in page.url, f"მოულოდნელი URL: {page.url}"