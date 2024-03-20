# Cria um programa que vai ler vários números e colocar em uma listo.
# Depois disso, crie duas listas extras que vão conter openas os volores
# pares e os voloras impores digitados respectivamente.
# No final, mostre o conteudo dos tres listas geradas.

# Solicita ao usuário que digite uma expressão matemática contendo parênteses.
expressao = str(input('Digite a expressão: '))

# Cria uma pilha vazia para rastrear a ordem dos parênteses.
pilha = []

# Itera sobre cada caractere na expressão digitada.
for simbolo in expressao:
    # Se encontrar um parêntese de abertura, adiciona à pilha.
    if simbolo == '(':
        pilha.append('(')
    # Se encontrar um parêntese de fechamento...
    elif simbolo == ')':
        # ...e se houver algum parêntese de abertura na pilha, remove-o.
        if len(pilha) > 0:
            pilha.pop()
        # Se não houver parênteses de abertura na pilha, a expressão está inválida.
        else:
            pilha.append(')')
            break

# Se a pilha estiver vazia ao final, significa que todos os parênteses de abertura foram fechados corretamente.
if len(pilha) == 0:
    print('Sua expressão está válida')
# Caso contrário, há parênteses de abertura sem o correspondente de fechamento, tornando a expressão inválida.
else:
    print('Sua expressão está inválida')
