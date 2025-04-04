# Riddle API (Flask + Firebase)

Este projeto é uma API RESTful construída com Flask e Firebase Firestore para gerenciar enigmas. Ele permite que os usuários obtenham enigmas aleatórios, pesquisem enigmas por ID, adicionem novos enigmas, atualizem enigmas existentes e excluam enigmas.

## Funcionalidades

-   **GET /riddles:** Retorna um enigma aleatório.
-   **GET /riddles/<id>:** Retorna um enigma específico pelo ID.
-   **POST /riddles:** Adiciona um novo enigma.
-   **PUT /riddles/<id>:** Atualiza um enigma existente.
-   **DELETE /riddles/<id>:** Exclui um enigma.

## Tecnologias Utilizadas

-   Python
-   Flask
-   Firebase Firestore
-   Flask-CORS
-   python-dotenv

## Pré-requisitos

-   Python 3.6+
-   Firebase Admin SDK
-   Flask
-   Flask-CORS
-   python-dotenv

## Configuração

1.  Clone este repositório.
2.  Instale as dependências:

    ```bash
    pip install Flask firebase-admin flask-cors python-dotenv
    ```

3.  Crie um arquivo `.env` na raiz do projeto e adicione as credenciais do Firebase:

    ```
    CONFIG_FIREBASE={"type": "service_account", "project_id": "seu-projeto-id", "private_key_id": "sua-chave-privada-id", "private_key": "-----BEGIN PRIVATE KEY-----\\nSUA_CHAVE_PRIVADA\\n-----END PRIVATE KEY-----\\n", "client_email": "seu-email-cliente", "client_id": "seu-id-cliente", "auth_uri": "[https://accounts.google.com/o/oauth2/auth](https://accounts.google.com/o/oauth2/auth)", "token_uri": "[https://oauth2.googleapis.com/token](https://oauth2.googleapis.com/token)", "auth_provider_x509_cert_url": "[https://www.googleapis.com/oauth2/v1/certs](https://www.googleapis.com/oauth2/v1/certs)", "client_x509_cert_url": "[https://www.googleapis.com/robot/v1/metadata/x509/seu-email-cliente](https://www.google.com/search?q=https://www.googleapis.com/robot/v1/metadata/x509/seu-email-cliente)", "universe_domain": "googleapis.com"}
    ```

    Substitua os valores pelos seus dados do Firebase.
    **Importante:** A private key dentro do json, deve ter todas as quebras de linha substituídas por \\n .

4.  Execute a aplicação:

    ```bash
    python app.py
    ```

## Endpoints

-   **GET /riddles**

    -   Retorna um enigma aleatório.
    -   Exemplo de resposta:

        ```json
        {
            "id": 1,
            "question": "Qual é a capital da França?",
            "answer": "Paris"
        }
        ```

-   **GET /riddles/<id>**

    -   Retorna um enigma específico pelo ID.
    -   Exemplo de resposta:

        ```json
        {
            "id": 1,
            "question": "Qual é a capital da França?",
            "answer": "Paris"
        }
        ```

-   **POST /riddles**

    -   Adiciona um novo enigma.
    -   Exemplo de requisição:

        ```json
        {
            "question": "Qual é a capital da Itália?",
            "answer": "Roma"
        }
        ```

    -   Exemplo de resposta:

        ```json
        {
            "message": "Riddle submitted successfully!"
        }
        ```

-   **PUT /riddles/<id>**

    -   Atualiza um enigma existente.
    -   Exemplo de requisição:

        ```json
        {
            "question": "Qual é a capital da Itália?",
            "answer": "Roma"
        }
        ```

    -   Exemplo de resposta:

        ```json
        {
            "message": "Riddle updated successfully"
        }
        ```

-   **DELETE /riddles/<id>**

    -   Exclui um enigma.
    -   Exemplo de resposta:

        ```json
        {
            "message": "Riddle deleted successfully!"
        }
        ```

## Autor

-   \[Seu Nome]

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
