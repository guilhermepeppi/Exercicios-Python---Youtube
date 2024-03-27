# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('\033[031mERRO! Digite um valor INTEIRO válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
