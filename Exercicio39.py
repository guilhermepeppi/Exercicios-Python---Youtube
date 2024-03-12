# Faça um programa que leia o ano de nascimanto de um jovem e informe
# da acordo com sua idado, se ele ainda vai sa alistar ao sarviço militar,
# se é a hora de se alistar ou sejá passou do tempo do alistamento.
# Seu programa também devará mostrar o tampo que falta ou que passou do prazo.

import datetime
ano_atual = datetime.date.today().year

ano_de_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_de_nascimento

if idade < 18:
    print(f'Quem nasceu em {ano_de_nascimento} tem '
          f'{idade} anos em {ano_atual}.')
    previsao_alistamento = 18 - idade
    print(f'Ainda faltam {previsao_alistamento} anos para o  alistamento')
    ano_do_alistamento = ano_atual - previsao_alistamento
    print(f'Seu alistamento será em {ano_do_alistamento}')
elif idade > 18:
    print(f'Quem nasceu em {ano_de_nascimento} tem {idade} em {ano_atual}')
    previsao_alistamento = idade - 18
    print(f'Você já deveria ter se alistado há {previsao_alistamento} anos.')
    ano_do_alistamento = ano_atual - previsao_alistamento
    print(f'Seu alistamento foi em {ano_do_alistamento}')
else:
    print(f'Quem nasceu em {ano_de_nascimento} tem '
          f'{idade} anos em {ano_atual}.')
    print(f'Você tem que se alistar IMEDIATAMENTE!')
