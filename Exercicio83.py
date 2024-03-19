# Crie um pragrama onde o usuário digite uma expressão qualquer que use parentases.
# Seu aplicativo devará analisar se a auprassão passado está com os parentases abertos e
# fachados no ordem correta.

# Solicita ao usuário que insira uma expressão contendo parênteses
expressao = input("Digite uma expressão contendo parênteses: ")

# Inicializa uma pilha para rastrear os parênteses abertos
pilha = []

# Percorre a expressão caractere por caractere
for char in expressao:
    # Se o caractere for um parêntese aberto, adiciona-o à pilha
    if char == '(':
        pilha.append(char)
    # Se o caractere for um parêntese fechado
    elif char == ')':
        # Verifica se há um parêntese aberto correspondente na pilha
        if not pilha:
            # Se não houver, os parênteses não estão balanceados corretamente
            print("Os parênteses não estão balanceados corretamente.")
            # Encerra o loop, pois não há necessidade de verificar mais a expressão
            break
        # Remove o parêntese aberto correspondente da pilha
        pilha.pop()
else:
    # Se o loop terminar sem interrupção, significa que todos os parênteses foram fechados corretamente
    # Verifica se a pilha está vazia, o que indica que todos os parênteses foram fechados corretamente
    if not pilha:
        # Se a pilha estiver vazia, os parênteses estão balanceados corretamente
        print("Os parênteses estão balanceados corretamente.")
    else:
        # Se ainda houver parênteses abertos na pilha, os parênteses não estão balanceados corretamente
        print("Os parênteses não estão balanceados corretamente.")
