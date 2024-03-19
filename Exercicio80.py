# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastra-los em uma lista ja no posição correta de inserçao (sam usar o sort).
# No final, mostre a listo ordanada na tela.

# Lista para armazenar os valores inseridos pelo usuário
valores = []

# Número de valores a serem inseridos
numero_valores = 5

# Loop para solicitar os valores do usuário
for i in range(numero_valores):
    # Solicita o valor ao usuário
    valor = int(input(f"Digite o {i + 1}º valor: "))

    # Se a lista estiver vazia, o valor é adicionado diretamente
    if not valores:
        valores.append(valor)
        print(f"Valor {valor} adicionado na primeira posição")
        continue

    # Posição inicial para busca na lista
    posicao = 0

    # Percorre a lista enquanto o valor for maior que o elemento atual
    # e a posição não ultrapassar o limite da lista
    while posicao < len(valores) and valor > valores[posicao]:
        posicao += 1

    # Insere o valor na posição correta da lista
    valores.insert(posicao, valor)

    # Exibe a mensagem com a posição de inserção
    print(f"Valor {valor} adicionado na posição {posicao + 1}")

# Mostra a lista ordenada na tela
print("Lista ordenada:", valores)
