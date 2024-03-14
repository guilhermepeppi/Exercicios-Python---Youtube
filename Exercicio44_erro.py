# # Elabore um programa que calcule o valor a ser pago por um produto.
# # considarando o seu preço normal e condição de pagamento:
# # - à vista dinheiro/cheque: 10% de dasconto
# # - à vista no cartão: 5% de desconto
# # - em ate 2x no cortao: preço normol
# # - 3x ou mais no cartão: 20% de juros


# Ao executar recebe erro:
#         match opcao:
#           ^
# SyntaxError: invalid syntax

def forma_de_pagamento(opcao, preco):
    match opcao:
        case 1:
            conta_preco_final = preco - (preco * 0.10)
            calculo_desconto = preco * 0.10
            print(f'Sua compra será à vista de COM DESCONTO de R${calculo_desconto}')
            print(f'Sua compra de R${preco} vai custar R${conta_preco_final} no final.')
        case 2:
            conta_preco_final = preco - (preco * 0.05)
            calculo_desconto = preco * 0.05
            parcelas = int(input('Quantas parcelas?: '))
            print(f'Sua compra será à vista no cartão de COM DESCONTO de R${calculo_desconto}')
            print(f'Sua compra de R${preco} vai custar R${conta_preco_final} no final.')
        case 3:
            conta_preco_final = preco
            parcelas = int(input('Quantas parcelas?: '))
            print(f'Sua compra será parcelada em {parcelas} de SEM JUROS')
            print(f'Sua compra de R${preco} vai custar R${conta_preco_final} no final.')
        case 4:
            conta_preco_final = preco + (preco * 0.20)
            calculo_juros = preco * 0.20
            parcelas = int(input('Quantas parcelas?: '))
            print(f'Sua compra será parcelada em {parcelas} de COM JUROS R${calculo_juros}')
            print(f'Sua compra de R${preco} vai custar R${conta_preco_final} no final.')
        case _:
            print('Escolha inválida')


preco_inicial = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção?: '))

forma_de_pagamento(opcao, preco_inicial)
