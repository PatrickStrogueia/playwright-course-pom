# Playwright Course — Page Object Model

Projeto de automação de testes E2E com [Playwright](https://playwright.dev/python/) e Python, utilizando o padrão **Page Object Model (POM)**. O sistema under test é o [SimulaBank](https://leogcarvalho.github.io/simulabank/login.html), uma aplicação bancária simulada.

---

## Tecnologias

- Python 3
- [pytest-playwright](https://playwright.dev/python/docs/test-runners)
- pytest

---

## Estrutura do projeto

```
playwright-course-pom/
├── conftest.py               # Fixtures globais (page, pages POM)
├── pytest.ini                # Configurações do pytest
├── requirements.txt          # Dependências
├── pages/                    # Page Objects
│   ├── common_page.py        # Ações e asserções comuns
│   ├── emprestimos_page.py   # Página de Empréstimos
│   ├── home_page.py          # Página inicial / menu
│   ├── login_page.py         # Página de Login
│   └── pix_page.py           # Página de Pix
└── tests/                    # Casos de teste
    ├── test_001_login_successful.py
    ├── test_002_fazer_pix.py
    ├── test_003_contratar_emprestimo.py
    ├── test_004_verificar_emprestimo_contratado.py
    └── test_005_verificar_pix_acima_limite.py
```

---

## Instalação

```bash
# 1. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Instale os browsers do Playwright
playwright install
```

---

## Executando os testes

### Todos os testes
```bash
pytest
```

### Com interface gráfica e slow motion
```bash
pytest --headed --slowmo 1000
```

### Um teste específico
```bash
pytest --headed --slowmo 1000 -k test_001_login_successful_pom
```

---

## Casos de teste

| Arquivo | Cenário |
|---|---|
| `test_001_login_successful.py` | Login com credenciais válidas |
| `test_002_fazer_pix.py` | Realizar transferência via Pix e verificar extrato |
| `test_003_contratar_emprestimo.py` | Contratar empréstimo e validar saldo |
| `test_004_verificar_emprestimo_contratado.py` | Bloquear novo empréstimo quando já existe um ativo |
| `test_005_verificar_pix_acima_limite.py` | Rejeitar Pix acima do limite de R$ 3.000,00 |

---

## Credenciais de teste

| Usuário | Senha |
|---|---|
| `user1` | `pass1` |