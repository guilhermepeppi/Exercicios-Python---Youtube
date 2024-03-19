# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior a o menor valor digitado e
# as suas respectivas posições no lista.

limite_maximo = 5
valores = []

try:
    # Loop para solicitar e armazenar os valores na lista
    for i in range(limite_maximo):
        valor = int(input('Digite um valor para a posição {}: '.format(i+1)))
        valores.append(valor)

    # Encontrar o valor máximo e suas posições
    maximo = max(valores)
    posicoes_maximo = []
    # Loop para encontrar todas as posições do valor máximo na lista

    # O uso de enumerate() neste caso nos permite obter tanto os valores quanto suas posições
    # na lista valores simultaneamente, o que é útil para encontrar as posições do valor máximo e mínimo.
    # Isso simplifica o código e o torna mais eficiente do que usar um loop convencional com um contador de índice.
    for i, valor in enumerate(valores):
        if valor == maximo:
            posicoes_maximo.append(i)

    # Encontrar o valor mínimo e suas posições
    minimo = min(valores)
    posicoes_minimo = []
    # Loop para encontrar todas as posições do valor mínimo na lista
    for i, valor in enumerate(valores):
        if valor == minimo:
            posicoes_minimo.append(i)

    # Imprimir os valores digitados, o valor máximo e mínimo, e suas posições
    print(f'Você digitou os valores: {valores}')
    print(f'O maior valor foi {maximo} na(s) posição(oes): {posicoes_maximo}')
    print(f'O menor valor foi {minimo} na(s) posição(oes): {posicoes_minimo}')

except ValueError:
    print("Erro: Digite apenas valores inteiros.")
