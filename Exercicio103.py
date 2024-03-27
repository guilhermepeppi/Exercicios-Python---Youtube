# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', qtde_gols=0):
    print(f'O jogador {nome} fez {qtde_gols} gol(s) no campeonato')


nome = str(input('Nome: '))
qtde_gols = str(input('Quantidade de gols: '))

if qtde_gols.isnumeric():
    qtde_gols = int(qtde_gols)
else:
    qtde_gols = 0

if nome.strip() == '':
    ficha(qtde_gols=qtde_gols)
else:
    ficha(nome, qtde_gols)
