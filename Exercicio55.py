# Faça um programa que leia o peso de cinco pessoas.
# # No final, mostre qual Foi o maior e o menor peso lidos.

maior_peso = float('-inf')
menor_peso = float('inf')

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

print(f'O maior peso lido foi de {maior_peso}kg')
print(f'O menor peso lido foi de {menor_peso}kg')
