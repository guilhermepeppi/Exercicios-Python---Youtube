# Escreva um programa que pergunte o salário de um funcionário e
# calcula o valor do seu aumanto.
# Para salários suparioras a R$1.250.00, calcula um aumento de 10%.
# Para os inferioras ou iguais, o aumento é de 15%

salario = float(input('Digite seu sário: '))

if salario >= 1250:
    salario += (salario * 0.10)
    print(f'Salário atualizado: R${salario:.2f}')
else:
    salario += (salario * 0.15)
    print(f'Salário atualizado: R${salario:.2f}')
