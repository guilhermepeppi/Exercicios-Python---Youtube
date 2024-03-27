# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():  # Verifica se a entrada é composta apenas por dígitos
            return int(entrada)
        else:
            print("Por favor, digite um valor numérico válido.")


n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')
