# Web Scraper

Este é um projeto simples de web scraping que extrai texto de páginas da web e salva em um arquivo.

## Como usar

1.  Certifique-se de ter o Python instalado.
2.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```
3.  Execute o script:

    ```bash
    python web_scraper.py
    ```

O resultado será salvo em `output.txt`.

## Arquivos

*   `web_scraper.py`: O script principal do web scraper.
*   `requirements.txt`: Lista as dependências do projeto.
*   `output.txt`: Arquivo de saída com o texto extraído das páginas.
*   `README.md`: Este arquivo.

## Observações

*   O script usa a biblioteca `requests` para fazer requisições HTTP e `beautifulsoup4` para analisar o HTML.
*   O script segue os links encontrados na página inicial e raspa o texto de cada página.
*   O script salva o texto de cada página em um arquivo `output.txt`.

## Próximos passos

*   Adicionar tratamento de erros mais robusto.
*   Permitir que o usuário especifique a URL inicial.
*   Adicionar opções para salvar os dados em outros formatos (JSON, CSV, etc.).
*   Adicionar suporte para autenticação em sites que exigem login.
