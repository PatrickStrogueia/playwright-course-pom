from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        # self.ver_extrato_button = page.get_by_role("button", name="Ver Extrato")
        # self.fazer_pix_button = page.get_by_role("button", name="Fazer Pix")

    def acessar_menu(self, menu):
        self.page.get_by_role("button", name=f"{menu}").click()

    # def assert_saldo_atual(self, saldo_atual_esperado):
    #     self.page.get_by_text(saldo_atual_esperado)
