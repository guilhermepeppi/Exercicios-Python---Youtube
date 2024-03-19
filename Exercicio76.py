# Crie um programa que tenha uma tupla única com nomes de produtos a seus respectivos
# preços, na sequencia.
# No final. mostre uma listagam de preços, organizando os dados em forma tabular.

# Tupla com nomes de produtos escolares e seus preços
produtos_escolares_precos = (
    "Lápis", 1.50,
    "Borracha", 0.80,
    "Caderno", 5.99,
    "Caneta", 2.25,
    "Régua", 1.99,
    "Estojo", 4.50,
    "Mochila", 29.99,
    "Apontador", 1.20,
    "Lápis de Cor", 3.50,
    "Cola", 1.75
)

# Imprimir a listagem de preços em forma tabular
print("-" * 40)
print(f"{'Listagem de Preços de Produtos Escolares':^40}")  # Título centralizado
print("-" * 40)

# Loop para imprimir os produtos e preços
for posicao in range(0, len(produtos_escolares_precos)):
    if posicao % 2 == 0:  # Se o índice for par (nome do produto)
        print(f'{produtos_escolares_precos[posicao]:.<30}', end='')  # Nome do produto alinhado à esquerda
    else:  # Se o índice for ímpar (preço do produto)
        print(f'R${produtos_escolares_precos[posicao]:>6}')  # Preço alinhado à direita
