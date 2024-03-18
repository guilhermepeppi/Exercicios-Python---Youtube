# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar a valor 999,
# que é a condição de parado.
# No final, mostre quantos números foram digitados e qual
# foi a soma entre clas (desconsiderando o flag).

soma = 0
contador = 0

while True:
    try:
        numero = int(input('Digite um número [999 para parar]: '))

        if numero == 999:
            break

        soma += numero
        contador += 1

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
