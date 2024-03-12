# Escrava um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador a em quantos anos ela vai pagar.
# A prestação mansal. neo pode axcader 30% do salário ou então o
# empréstimo será negado.

valor_da_casa = float(input('Valor da casa: R$'))
salario_do_comprador = float(input('Salário do comprador: R$'))
anos_de_financiamento = float(input('Quantos anos de financiamento?: '))

prestacao = valor_da_casa / (anos_de_financiamento * 12)

print(f'Para pagar uma casa de R${valor_da_casa:.2f} em '
      f'{anos_de_financiamento:.0f} anos a prestação será de R${prestacao:.2f}')

if prestacao > (salario_do_comprador * 0.30):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
