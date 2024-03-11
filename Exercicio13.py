salario = float(input('Qual é o salário do Funcionário? '))  # R$4319.43

salario_reajustado = salario + (salario * 0.15)

print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salario_reajustado:.2f}')  # R$4967.34
