# Site Status Checker
 **PT-BR**

🔍 **Descrição**
 - Script em Python para verificar a acessibilidade de sites.

✨ **Funcionalidades**
 - Testar se um site está acessível.
 - Personalizar o tempo máximo de espera pela resposta.

🛠️ **Tecnologias Utilizadas**
 - Python 3.12.8

📚 **Bibliotecas**
 - Requests

🏗️ **Estrutura do Código**

Importação de Bibliotecas:
 - Utiliza a biblioteca `requests` para realizar requisições HTTP.

Funções Principais:
 - `verify_site(url: str, timer: int = 5) -> str`: Verifica se um site está acessível, retornando seu status HTTP ou um erro caso não esteja disponível.

Programa Principal:
 - Solicita ao usuário a URL do site.
 - Chama a função `verify_site` para testar a acessibilidade do site.
 - Exibe o status do site ao usuário.

---

**EN-US**

🔍 **Description**
 - Python script to check website accessibility.

✨ **Features**
 - Check if a website is accessible.
 - Customize the maximum wait time for a response.

🛠️ **Technology** 
 - Python 3.12.8

📚 **Libraries**
 - Requests

🏗️ **Code Structure**

Library Import:
 - Uses the `requests` library to perform HTTP requests.

Main Functions:
 - `verify_site(url: str, timer: int = 5) -> str`: Checks if a website is accessible, returning its HTTP status or an error if unavailable.

Main Program:
 - Asks the user for the website URL.
 - Calls the `verify_site` function to test website accessibility.
 - Displays the website status to the user.

