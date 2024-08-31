# My Webserver

Este é um aplicativo básico construído com o Flask. Ele serve como ponto de partida para o desenvolvimento de aplicações web mais complexas. A estrutura do projeto é modular e escalável, permitindo a fácil adição de novas funcionalidades.

## Estrutura do Projeto

```
my_webserver/
├── .venv/                   # Ambiente virtual para dependências do projeto
├── app/                     # Diretório principal da aplicação
│   ├── __init__.py          # Inicializa o aplicativo Flask
│   ├── routes.py            # Define as rotas/endpoints
├── static/                  # Arquivos estáticos (CSS, JS, imagens, etc.)
│   └── style.css            # Exemplo de arquivo CSS
├── templates/               # Templates HTML (Jinja2)
│   └── home.html            # Exemplo de arquivo de template
├── .gitignore               # Arquivos e pastas a serem ignorados pelo Git
├── config.py                # Configurações da aplicação
├── requirements.txt         # Dependências do projeto (usado com pip)
├── run.py                   # Ponto de entrada para rodar o servidor Flask
└── test_app.py              # Arquivo de teste para o aplicativo
```

## Funcionalidades

- **Rotas Definidas:**
  - **`/`:** Renderiza a página `home.html` localizada em `templates/`.
  - **`/test`:** Retorna uma string simples `"this is a test"`.

- **Estrutura Modular:** O projeto está organizado de forma que seja fácil adicionar novas funcionalidades, como rotas, modelos de dados, e arquivos estáticos.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/my_webserver.git
   cd my_webserver
   ```

2. **Crie e ative o ambiente virtual:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Como Rodar

1. **Inicie o servidor Flask:**

   ```bash
   python run.py
   ```

2. **Acesse o aplicativo:**
   - Abra seu navegador e acesse `http://127.0.0.1:5000/` para ver a página inicial.
   - Acesse `http://127.0.0.1:5000/test` para ver a página de teste.

## Testes

1. **Rodando os testes:**

   Execute os testes para garantir que tudo está funcionando conforme o esperado:

   ```bash
   python test_app.py
   ```

2. **Resultados esperados:**

   Todos os testes devem passar, indicando que as rotas estão funcionando corretamente.

## Configurações

- **config.py:** Contém configurações globais do aplicativo, como `SECRET_KEY`, configurações de banco de dados e outros parâmetros de configuração.

## Próximos Passos

- **Adicionar novas rotas e funcionalidades.**
- **Expandir o uso de banco de dados e autenticação.**
- **Implementar testes mais abrangentes à medida que o projeto cresce.**

## Contribuições

Sinta-se à vontade para abrir issues ou pull requests no repositório se quiser contribuir com melhorias ou novas funcionalidades.
