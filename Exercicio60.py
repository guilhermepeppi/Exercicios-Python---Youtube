# Faça um programa que leia um número qualquar a mostra o seu fatorial

# USANDO MATH

# from math import factorial

# numero = int(input('Digite um número para calcular seu faltorial: '))
# fatorial = factorial(numero)

# print(f'O fatorial de {numero} é {fatorial}')

# SEM MATH

numero = int(input('Digite um número para calcular seu faltorial: '))

calculo = numero
fatorial = 1

print(f'Calculando {numero}! = ', end='')

while calculo > 0:
    print(f'{calculo} ', end='')
    print(' x ' if calculo > 1 else ' = ', end='')
    fatorial *= calculo
    calculo -= 1

print(f'{fatorial}')
