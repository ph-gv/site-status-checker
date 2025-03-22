# BIBLIOTECAS USADAS
import requests
from requests.exceptions import RequestException

# FUNÇÃO
def verify_site(url: str, timer: int = 5) -> str:
    """
    -->Testa se um site está ou não acessível.
    :arg url: domínio a ser testado.
    :arg timer: Tempo máximo de espera pela resposta em segundos (padrão 5).
    :return: Status do Site.
    """
    try:
        if not url.startswith(('http://', 'https://')):
            url = f'https://{url}'
        asnwer = requests.get(url, timeout=timer)
        asnwer.raise_for_status()
        print('-=-'*8)
        return f"""\033[32mO site está acessível.\033[m
Status: {asnwer.status_code}"""
    except RequestException as error:
        print('-=-'*12)
        return f"""\033[31mO site está inacessível no momento.\033[m 
Erro: {error}""" 


# PROGRAMA PRINCIPAL
print(f'\033[33mURL do Site:\033[m')
link = verify_site(input('> ')).strip()
print(link)
