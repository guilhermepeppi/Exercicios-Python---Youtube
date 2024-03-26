# Crie um programa que tenha uma função fatorial()
# que receba dois parametros, o primeiro que indique o número a calcular
# e o outro chamado show, que será um valor lógico (opcional) indicando
# se será mostrado ou não na tela o processo de cálculo do fatorial.


# Definição da função fatorial
def fatorial(numero, show=False):
    print('-=' * 20)
    resultado = 1
    if show:
        print(f'Calculando o fatorial de {numero}:')
    for i in range(1, numero + 1):
        resultado *= i
        if show:
            if i < numero:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = ', end='')
    if show:
        print(resultado)
    else:
        print(f'Fatorial de {numero}: {resultado}')


fatorial(5)

fatorial(6, show=True)
