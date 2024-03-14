# Crie um programa que mostra na tala todos os
# números paras que astão no intervalo entre 1 a 50.

lista = list(range(1, 50))

for numero in lista:
    if numero % 2 == 0:
        print(numero, end=' ')
