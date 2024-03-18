# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
# elementos de uma Sequência de Fibonacci.
# Ек:
# 0 → 1 → 1 → 2 → 3 → 5 → 8

print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)

n = int(input('Quantos termos você quer mostrar?: '))

t1 = 0
t2 = 1

print(f'{t1} → {t2}', end='')

contador = 3  # os dois primeiros números são sempre 0 e 1 consecutivamente.
while contador <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' → FIM')
