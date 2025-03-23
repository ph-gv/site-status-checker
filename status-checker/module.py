# BIBLIOTECAS USADAS
import requests
from requests.exceptions import RequestException

# FUNÇÃO
def verify_site(timer: int = 5) -> str:
    """
    -->Testa se um site está ou não acessível.
    :arg timer: Tempo máximo de espera pela resposta em segundos (padrão 5).
    :return: Status do Site.
    """
    url = str(input(f'\033[33mURL >\033[m ')).lower().strip()
    try:
        # CASO USUARIO NÃO DIGITE O LINK DE FORMA COMPLETA
        if not url.startswith(('http://', 'https://')):
            url = f'https://{url}'
        if not url.endswith(('.com')):
            url = f'{url}.com'
        # VERIFICAÇÃO DE ACESSIBILIDADE DO DOMINIO
        asnwer = requests.get(url, timeout=timer)
        asnwer.raise_for_status()
        print('-=-'*8)
        return f"""\033[32mO site está acessível.\033[m
Status: {asnwer.status_code}"""
    except RequestException as error:
        print('-=-'*12)
        return f"""\033[31mO site está inacessível no momento.\033[m 
Erro: {error}""" 


def verify_multiples_sites(timer: int = 5) -> str:
    """
    -->Testa se múltiplos sites estão ou não acessíveis.
    :arg timer: Tempo máximo de espera pela resposta em segundos (padrão 5).
    :return (print): Status do Site.
    """
    while True:
        try:
            amount_of_sites = int(input("""Qtd. de Sites 
> """))
            break
        except ValueError:
            print(f'\033[31m[ERRO] Dados Inválidos\033[m')
    
    domains = list()
    for i in range(0,amount_of_sites):
        domains.append(str(input(f'{i+1}º Site: ')).lower().strip())
    
    for url in domains:
        try:
            # CASO USUARIO NÃO DIGITE O LINK DE FORMA COMPLETA
            if not url.startswith(('http://', 'https://')):
                url = f'https://{url}'
            if not url.endswith(('.com')):
                url = f'{url}.com'
            # VERIFICAÇÃO DE ACESSIBILIDADE DO DOMINIO
            asnwer = requests.get(url, timeout=timer)
            asnwer.raise_for_status()
            print('-=-'*8)
            print(f"""\033[32mO site {url} está acessível.\033[m
Status: {asnwer.status_code}""")
        except RequestException as error:
            print('-=-'*12)
            print(f"""\033[31mO site {url} está inacessível no momento.\033[m 
Erro: {error}""")


def l() -> str:
    print('---'*8)
