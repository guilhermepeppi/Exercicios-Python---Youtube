def forma_de_pagamento(opcao, preco):
    if opcao == 1:
        conta_preco_final = preco - (preco * 0.10)
        calculo_desconto = preco * 0.10
        print(f'Sua compra será à vista COM DESCONTO de R${calculo_desconto:.2f}')
        print(f'Sua compra de R${preco:.2f} vai custar R${conta_preco_final:.2f} no final.')
    elif opcao == 2:
        conta_preco_final = preco - (preco * 0.05)
        calculo_desconto = preco * 0.05
        parcelas = int(input('Quantas parcelas?: '))
        print(f'Sua compra será à vista no cartão COM DESCONTO de R${calculo_desconto:.2f}')
        print(f'Sua compra de R${preco:.2f} vai custar R${conta_preco_final:.2f} no final.')
    elif opcao == 3:
        conta_preco_final = preco
        parcelas = int(input('Quantas parcelas?: '))
        print(f'Sua compra será parcelada em {parcelas} vezes SEM JUROS')
        valor_parcela = conta_preco_final / parcelas
        print(f'Cada parcela será de R${valor_parcela:.2f}. Total: R${conta_preco_final:.2f}')
    elif opcao == 4:
        conta_preco_final = preco + (preco * 0.20)
        calculo_juros = preco * 0.20
        parcelas = int(input('Quantas parcelas?: '))
        print(f'Sua compra será parcelada em {parcelas} vezes COM JUROS de R${calculo_juros:.2f}')
        valor_parcela = conta_preco_final / parcelas
        print(f'Cada parcela será de R${valor_parcela:2.f}. Total: R${conta_preco_final:.2f}')
    else:
        print('Escolha inválida')


preco_inicial = float(input('Preço das compras R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção?: '))

forma_de_pagamento(opcao, preco_inicial)
