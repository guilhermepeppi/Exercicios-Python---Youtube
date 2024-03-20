# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores paras digitados.
# B) A somo dos valores da terceira coluna.
# C) 0 maior valor da segunda linha.

matriz = []
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = None

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para a posição ({i+1}, {j+1}): '))
        linha.append(valor)
        if valor % 2 == 0:  # Verifica se o valor é par
            soma_pares += valor
        if j == 2:  # Verifica se está na terceira coluna
            soma_terceira_coluna += valor
        if i == 1:  # Verifica se está na segunda linha
            if maior_valor_segunda_linha is None or valor > maior_valor_segunda_linha:
                maior_valor_segunda_linha = valor
    matriz.append(linha)

print("Matriz 3x3:")
for linha in matriz:
    print(linha)

print(f'A) Soma de todos os valores pares: {soma_pares}')
print(f'B) Soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'C) Maior valor da segunda linha: {maior_valor_segunda_linha}')
