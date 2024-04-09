def leiaInt(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pela usuário.\033[m')
            return 0
        else:
            return entrada


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    opcao = leiaInt('\n\033[32mSua opcão:  \033[m')
    return opcao
