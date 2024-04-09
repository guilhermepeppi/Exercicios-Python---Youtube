# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
# possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# também uma função leiaFloat() com a mesma funcionalidade.
# -----
# Exercicio 104:
# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

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


def leiaFloat(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pela usuário.\033[m')
            return 0
        else:
            return entrada


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Número inteiro: {n1}')
print(f'Número real: {n2}')
