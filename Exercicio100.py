# Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar().
# A primaira função vai sortear 5 números a vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos
# os valores PARES sortcados pela função anterior.

import random


def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(random.randint(1, 100))
    return numeros


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma


# Testando as funções
numeros_sorteados = sorteia()
print("Números sorteados:", numeros_sorteados)
soma_pares = somaPar(numeros_sorteados)
print("Soma dos números pares sorteados:", soma_pares)
