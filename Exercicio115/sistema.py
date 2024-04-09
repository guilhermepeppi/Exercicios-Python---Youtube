# Vamos criar um menu em Python, usando modularização.
# Crie um pequeno sistema modularizado que permita cadastrar passoas pelo seu
# nome e idade em um arquivo de texto simplas. O sistema só vai ter 2 opcoes:
# 1) Cadastrar uma nova passoa;
# 2) Listar todas as pessoas cadastradas.

from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if arquivoExiste(arquivo):
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')

while True:
    resposta = menu(['Ver pessoas cadastradas',
                     'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1)
