
print('=' * 20)
txt = 'SISTEMA LOJA'
new_str = txt.center(20, ' ')
print(new_str)
print('=' * 20)

total_compra = 0
total_produtos_mil_reais = 0
preco_produto_mais_barato = float('inf')
nome_produto_mais_barato = ''

while True:
    nome_produto = str(input('Nome do Produto: '))
    preco_produto = float(input('Preço R$'))
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    total_compra += preco_produto

    if preco_produto > 1000:
        total_produtos_mil_reais += 1

    if preco_produto < preco_produto_mais_barato:
        preco_produto_mais_barato = preco_produto
        nome_produto_mais_barato = nome_produto

    while escolha not in 'SsNn':
        print('Escolha incorreta!')
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if escolha == 'N':
        break

print(f'O total da compra foi R${total_compra:.2f}')
print(f'Temos {total_produtos_mil_reais} produtos custando mais R$1.000,00')
print(f'O produto mais barato foi {nome_produto_mais_barato} que custa R${preco_produto_mais_barato:.2f}')
