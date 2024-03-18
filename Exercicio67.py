# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado palo usuário.
# O programa será interrompido quando o númaro solicitado for negativo.

contador = 1
total = 0

while True:
    try:
        tabuada = int(input('Tabuada do número: '))
        if tabuada < 0:
            print('Encerrando...')
            break
        for contador in range(1, 11):
            total = tabuada * contador
            print(f'{tabuada} x {contador} = {total}')
    except ValueError:
        print('Digite um número inteiro!')
