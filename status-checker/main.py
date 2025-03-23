# IMPORTAÇÃO DE MÓDULO
import module as md

# PROGRAMA PRINCIPAL
print(f"{'Site Status Checker':^20}")
while True:
    try:
        user_asnwer = int(input("""[1] Um site
[2] Múltiplos Sites
[3] Encerrar Programa
> """))
        md.l()
        if user_asnwer < 1 or user_asnwer > 3:
            print(f'\033[31m[ERRO] Dados Inválidos\033[m')
        if user_asnwer==1:
            link = md.verify_site()
            print(link)
            md.l()
        if user_asnwer==2:
            md.verify_multiples_sites()
            md.l()
        if user_asnwer==3:
            print('PROGRAMA ENCERRADO...')
            break
    except ValueError:
        print(f'\033[31m[ERRO] Dados Inválidos\033[m')
