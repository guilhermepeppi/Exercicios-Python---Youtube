# Cria um programa que leia o ano da nascimanto de sete passoas.
# No Final, mostre quantas passoas ainda não atingiram a maioridada e
# quantas já são maioras

from datetime import date
ano_atual = date.today().year

total_maior = 0
total_menor = 0

for numero_pessoas in range(1, 8):
    ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu?: '.format(numero_pessoas)))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1

print()
print(f'Numero de pessoas maiores de idade: {total_maior}')
print(f'Numero de pessoas menores de idade: {total_menor}')
