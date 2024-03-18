# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valoras
# e qual foi o maior e o menor valoras lidos.
# O programa dave perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = 0
total_numeros = 0
maior_numero = float('-inf')
menor_numero = float('inf')
continuar = 'S'

while continuar in 'Ss':
    try:
        numero = int(input('Digite um número: '))
        soma += numero
        total_numeros += 1

        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

    while True:
        continuar = input('Quer continuar? [S/N]: ').upper().strip()
        if continuar in ['S', 'N']:
            break
        else:
            print("Por favor, digite apenas 'S' ou 'N'.")

    if continuar == 'N':
        break

media = soma / total_numeros if total_numeros != 0 else 0

print(f'Você digitou {total_numeros} números.')
print(f'A média entre eles foi {media:.2f}.')
print(f'O menor número digitado foi {menor_numero} e o maior foi {maior_numero}.')
