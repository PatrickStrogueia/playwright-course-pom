# from playwright.sync_api import Page, expect


# def test_001_login_successful(page: Page) -> None:
#     page.goto("https://leogcarvalho.github.io/simulabank/login.html")
#     page.get_by_role("textbox", name="Usuário:").fill("user1")
#     page.get_by_role("textbox", name="Senha:").fill("pass1")
#     page.get_by_role("button", name="Entrar").click()
#     expect(page.get_by_role("heading", name="Bem-vindo ao SimulaBank!")).to_be_visible()

def test_001_login_successful_pom(login_page) -> None:
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()

# pytest --headed --slowmo 1000 -k test_001_login_successful_pom