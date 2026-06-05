import pytest
from pages.login_page import LoginPage

@pytest.fixture
def page(page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")
    return page

@pytest.fixture
def login_page(page):
    return LoginPage(page)
