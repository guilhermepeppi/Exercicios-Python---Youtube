from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.readlines())
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.wirte(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
