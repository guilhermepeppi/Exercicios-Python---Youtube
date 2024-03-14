# Crie um programa que faça o computador
# jogar Jokenpô com você

import random

# Opções do jogo
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

while True:
    print('Suas opções:')
    print('[ 0 ] PEDRA')
    print('[ 1 ] PAPEL')
    print('[ 2 ] TESOURA')

    jogada = int(input('Qual é a sua jogada?: '))

    # Verificando a entrada do usuário
    if jogada < 0 or jogada > 2:
        print('Jogada inválida! Escolha um número entre 0 e 2.')
        continue

    # Escolha aleatória para o computador
    jogada_computador = random.randint(0, 2)

    # Imprimindo as jogadas
    print('\nJO KEN PO!!!')
    print('ー' * 7)
    print(f'Computador jogou {opcoes[jogada_computador]}')
    print(f'Jogador jogou {opcoes[jogada]}')
    print('ー' * 7)

    # Verificando o resultado
    if jogada == jogada_computador:
        print('Empate!')
    elif (jogada == 0 and jogada_computador == 2) or \
         (jogada == 1 and jogada_computador == 0) or \
         (jogada == 2 and jogada_computador == 1):
        print('Jogador vence!')
    else:
        print('Computador vence!')

    # Pergunta ao jogador se ele deseja jogar novamente
    jogar_novamente = input('Deseja jogar novamente? (s/n): ')
    if jogar_novamente.lower() != 's':
        break
