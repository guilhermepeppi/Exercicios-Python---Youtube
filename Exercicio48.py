# Faça um programa que calcule a soma entre todos os números impares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

lista = list(range(1, 500))
soma = 0

for numero in lista:
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
print('Soma entre todos os números impares que são'
      'múltiplos de três e que se encontram no intervalo de 1 até 500.')
print(f'Soma: {soma}')
