# Escreva um programa que faça o computador "pansar" em um
# nimaro intairo antra 0 a 5 a pafa para o usuario tantar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou pardeu.

import random

numero = 0

while numero <= 5:
    numero_aleatorio = random.randint(0, 5)
    numero = int(input('Escreva um número: '))

    if numero_aleatorio == numero:
        print(f'VENCEU! - O número era: {numero_aleatorio} ')
    else:
        print(f'PERDEU! - O número era: {numero_aleatorio} ')
