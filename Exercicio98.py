# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: inicio, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 am 2
# c) Uma contagem personalizado.

from time import sleep


def contador(inicio, fim, passo):
    if passo <= 0:
        while passo <= 0:
            passo = int(input("Erro: O passo deve ser maior que zero. Insira um novo valor para o passo: "))
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=' ➙ ', flush=True)
            sleep(0.5)
            inicio += passo
        print('FIM')
    else:
        while inicio >= fim:
            print(inicio, end=' ➙ ', flush=True)
            sleep(0.5)
            inicio -= passo
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Personalizar contagem:')
print()

try:
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    contador(inicio, fim, passo)
except ValueError:
    print("Erro: Insira um valor numérico válido para início, fim e passo.")

print('-=' * 20)
