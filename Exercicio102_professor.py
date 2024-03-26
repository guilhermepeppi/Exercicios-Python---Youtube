# Crie um programa que tenha uma função fatorial()
# que receba dois parametros, o primeiro que indique o número a calcular
# e o outro chamado show, que será um valor lógico (opcional) indicando
# se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero, show=False):
    f = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= contador
    return f


print('-=-' * 12)
print(fatorial(5, show=False))
print('-=-' * 12)
print(fatorial(8, show=True))
print('-=-' * 12)
