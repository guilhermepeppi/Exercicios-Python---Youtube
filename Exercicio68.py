# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas qua ele conquistou no final do jogo.

from random import randint

total_vitorias = 0

print('=' * 25)
print('JOGO PAR OU IMPAR')
print('=' * 25)

while True:
    try:
        print()
        valor_jogador = int(input('Digite um valor: '))
        valor_computador = randint(0, 10)
        total = valor_jogador + valor_computador
        escolha_jogador = input('Par ou impar? [P/I]: ').strip().upper()[0]
        while escolha_jogador not in 'PpIi':
            escolha_jogador = input('Par ou impar? [P/I]: ').strip().upper()[0]
        print('-' * 25)
        print(f'Você jogou {valor_jogador} e o computador {valor_computador}, total {total}')
        if (total % 2 == 0 and escolha_jogador == 'P') or (total % 2 != 0 and escolha_jogador == 'I'):
            print('Você venceu!')
            total_vitorias += 1
        else:
            print('Você perdeu!')
            print(f'GAME OVER! Você venceu {total_vitorias} vezes')
            break
        print('Vamos jogar novamente....')

    except ValueError:
        print('Valor inválido, tente novamente')
