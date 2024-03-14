# Dasenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daquelas que foram pares.
# Se o valor digitado for impar dasconsidera-o.

soma = 0

for numero in range(6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero

print(f'\nSoma dos numeros pares: {soma}')
