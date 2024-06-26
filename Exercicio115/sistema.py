# Vamos criar um menu em Python, usando modularização.
# Crie um pequeno sistema modularizado que permita cadastrar passoas pelo seu
# nome e idade em um arquivo de texto simplas. O sistema só vai ter 2 opcoes:
# 1) Cadastrar uma nova passoa;
# 2) Listar todas as pessoas cadastradas.

from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                     'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Listar conteudo do arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        # Cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1)
