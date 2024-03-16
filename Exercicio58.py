# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entra 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que voce consegue adavanhar qual foi?')

numero_aleatorio = randint(0, 10)
palpite = -1
tentativas = 0

while palpite != numero_aleatorio:
    palpite = int(input('Qual é o seu palpite? '))
    tentativas += 1

    if palpite < numero_aleatorio:
        print('Mais... Tente mais uma vez.')
    elif palpite > numero_aleatorio:
        print('Menos... Tente mais uma vez.')
    else:
        print(f'Acertou com {tentativas} tentativa(s). Parabéns!')
