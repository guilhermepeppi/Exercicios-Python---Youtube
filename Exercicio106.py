# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores.

from time import sleep

cores = ('\033[m',  # Sem cores
         '\033[0;30;41m',  # Vermelho
         '\033[0;30;42m',  # Verde
         '\033[0;30;43m',  # Amarelo
         '\033[0;30;44m',  # Azul
         '\033[0;30;45m',  # Roxo
         '\033[7;30m'  # Branco
         )


def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(cores[6], end='')
    help(comando)
    print(cores[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(cores[0], end='')
    sleep(1)


comando = ''

while True:
    titulo('SISTEMA DE AJUDA pyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
