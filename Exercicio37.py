# Escrava um programa que laia um númaro inteiro qualquer a pasa para o
# usuário escolher qual sará a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)}')
else:
    print('Opção Inválida!')
