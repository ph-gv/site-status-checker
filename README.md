# Site Status Checker
**PT-BR**

🔍 **Descrição**  
 - Automação de verificação de status de sites, implementada em Python. O programa permite testar a acessibilidade de um único site ou de múltiplos sites através de uma interface de linha de comando.

✨ **Funcionalidades**  
 - Verificar se um único site está acessível  
 - Verificar se múltiplos sites estão acessíveis  
 - Validação e ajuste automático do URL (adição de "https://" e ".com", se necessário)  
 - Exibição de mensagens com códigos de status HTTP e erros, quando aplicável

🛠️ **Tecnologias Utilizadas**  
 - Python 3.12.8

📚 **Bibliotecas**  
 - requests

🏗️ **Estrutura do Código**  

**main.py**  
 - **Importação de Módulo:**  
   - Importa o módulo `module` (renomeado como `md`) para utilizar as funções de verificação e utilitários.
 - **Programa Principal:**  
   - Exibe o título "Site Status Checker" centralizado.  
   - Apresenta um menu interativo com três opções:  
     1. Verificar um site  
     2. Verificar múltiplos sites  
     3. Encerrar o programa  
   - Trata entradas inválidas e chama as funções do módulo conforme a escolha do usuário.

**module.py**  
 - **Importação de Bibliotecas:**  
   - Utiliza a biblioteca `requests` para realizar requisições HTTP e tratar exceções com `RequestException`.
 - **Funções Principais:**  
   - `verify_site(timer: int = 5) -> str`:  
     Solicita a URL, ajusta o formato (incluindo `https://` e `.com` se necessário) e verifica a acessibilidade do site, retornando uma mensagem com o status.
   - `verify_multiples_sites(timer: int = 5) -> str`:  
     Permite ao usuário informar a quantidade de sites e as URLs correspondentes, verificando a acessibilidade de cada um e exibindo os respectivos status.
   - `l() -> str`:  
     Imprime um separador visual para organizar a saída no terminal.

---

**EN-US**

🔍 **Description**  
 - Site status checker automation implemented in Python. This command-line tool allows you to test the accessibility of a single website or multiple websites.

✨ **Features**  
 - Check if a single site is accessible  
 - Check if multiple sites are accessible  
 - Automatic URL validation and adjustment (adds "https://" and ".com" if missing)  
 - Displays messages with HTTP status codes and error details when applicable

🛠️ **Technology**  
 - Python 3.12.8

📚 **Library**  
 - requests

🏗️ **Code Structure**  

**main.py**  
 - **Module Import:**  
   - Imports the `module` (aliased as `md`) to use its verification functions and utilities.
 - **Main Program:**  
   - Displays the centered title "Site Status Checker".  
   - Presents an interactive menu with three options:  
     1. Check one site  
     2. Check multiple sites  
     3. Exit the program  
   - Handles invalid input and calls the corresponding functions from the module based on the user's choice.

**module.py**  
 - **Library Import:**  
   - Uses the `requests` library to perform HTTP requests and handle exceptions using `RequestException`.
 - **Main Functions:**  
   - `verify_site(timer: int = 5) -> str`:  
     Prompts for a URL, adjusts its format (adding `https://` and `.com` if needed), and checks the site's accessibility, returning a message with its status.
   - `verify_multiples_sites(timer: int = 5) -> str`:  
     Asks the user for the number of sites and their URLs, then checks each site’s accessibility and displays the respective status.
   - `l() -> str`:  
     Prints a visual separator to organize the terminal output.