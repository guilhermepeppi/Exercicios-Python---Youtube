# Faça um programa que leia três números
# a mostra qualé o maior a qual é o menor.

primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
terceiro_valor = int(input('Terceiro valor: '))

# menor valor
if primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
    print(f'O menor valor digitado foi {primeiro_valor}')
elif segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    print(f'O menor valor digitado foi {segundo_valor}')
else:
    print(f'O menor valor digitado foi {terceiro_valor}')

# maior valor
if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
    print(f'O maior valor digitado foi {primeiro_valor}')
elif segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    print(f'O maior valor digitado foi {segundo_valor}')
else:
    print(f'O maior valor digitado foi {terceiro_valor}')
