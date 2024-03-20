# Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# Criando uma matriz vazia de dimensão 3x3
matriz = []

# Preenchendo a matriz com valores lidos pelo teclado
for i in range(3):  # Percorre as linhas da matriz (índices 0, 1 e 2)
    linha = []  # Cria uma lista vazia para representar uma linha da matriz
    for j in range(3):  # Percorre as colunas da matriz (índices 0, 1 e 2)
        # Pede ao usuário para inserir o valor para a posição (i, j)
        valor = int(input(f'Digite o valor para a posição ({i+1}, {j+1}): '))
        linha.append(valor)  # Adiciona o valor à linha atual da matriz
    matriz.append(linha)  # Adiciona a linha preenchida à matriz

# Exibindo a matriz preenchida com linhas separadas
print("Matriz 3x3:")
for linha in matriz:  # Percorre cada linha da matriz
    print(linha)  # Exibe a linha
