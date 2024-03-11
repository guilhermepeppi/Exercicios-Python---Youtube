valor_produto = float(input('Qual é o preço do produto? '))  # R$123.95

valor_desconto = (valor_produto * 0.05)
novo_preco = valor_produto - valor_desconto

print(f'o produto que custava R${valor_produto}, na promoção com desconto de 5% vai custar R${novo_preco:.2f}')
