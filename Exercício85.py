# Crie um programa onde o usuário possa digitar sete valoras numéricos
# e cadastra-los em uma lista única que mantenha separados
# os valores pares e impares.
# No final. mostre os valores pares a impares em ordem crescente.

# Lista para armazenar os números, onde cada sublista representa os números pares e ímpares
lista = [[], []]

for numero in range(1, 8):
    numero_digitado = int(input(f'Digite o {numero}º número: '))
    if numero_digitado % 2 == 0:
        lista[0].append(numero_digitado)  # Adiciona o número par à primeira sublista
    else:
        lista[1].append(numero_digitado)  # Adiciona o número ímpar à segunda sublista

# Ordena os números pares e ímpares em ordem crescente
lista[0].sort()
lista[1].sort()

print("Números pares:", lista[0])
print("Números ímpares:", lista[1])
