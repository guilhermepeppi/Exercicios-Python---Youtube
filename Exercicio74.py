# Crie um programa que vai gerar cinco números aleatórios e
# colocar em uma tupla. Depois disso, mostra a listagem de números gerados e também indique
# o menor a o maior valor que estao na tupla.

from random import randint

# Cria uma lista vazia para armazenar os números aleatórios
lista = []

# Gera cinco números aleatórios e os coloca na lista
for i in range(5):
    numero_aleatorio = randint(0, 50)
    lista.append(numero_aleatorio)

# Converte a lista em uma tupla
valores_aleatorios = tuple(lista)

# Exibe a listagem de números gerados
print("Números aleatórios:", valores_aleatorios)

# Exibe o menor e o maior valor da tupla
print("Menor valor:", min(valores_aleatorios))
print("Maior valor:", max(valores_aleatorios))
