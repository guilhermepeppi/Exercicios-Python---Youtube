# Cria um programa que vai ler vários números e colocar em uma listo.
# Depois disso, crie duas listas extras que vão conter openas os volores
# pares e os voloras impores digitados respectivamente.
# No final, mostre o conteudo dos tres listas geradas.

expressao = str(input('Digite a expressão: '))

pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')
