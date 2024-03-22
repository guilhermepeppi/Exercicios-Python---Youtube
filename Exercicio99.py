# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valoras inteiros.
# Seu programa tem que analisar todos os valoras e dizer qual deles é o maior.

from random import randint


def maior(*numeros):
    if len(numeros) == 0:
        print("Nenhum número foi fornecido.")
    else:
        quantidade_valores = len(numeros)
        maior_numero = max(numeros)

        print("Analisando os valores passados...")
        print("Valores informados:", end=" ")
        for num in numeros:
            print(num, end=" ")
        print()
        print("Foram informados", quantidade_valores, "valores ao todo.")
        print("O maior valor informado foi", maior_numero)


quantidade_numeros = randint(1, 10)
# Gerando os números aleatórios
numeros_aleatorios = [randint(1, 100) for _ in range(quantidade_numeros)]

maior(*numeros_aleatorios)
