# Cria um programa que simula o funcionamento de um caixa aletrônico.
# No inicio, pergunta ao usuario qual sara o valor a ser sacado (numero
# inteiro) a o programa vai informar quantas cédulas de cada valor serão entreguas

# Imprime o cabeçalho do caixa eletrônico
print('=' * 30)
print('{:^30}'.format('BANCO DEV'))
print('=' * 30)

# Solicita ao usuário o valor a ser sacado e converte para inteiro
valor_sacado = int(input('Qual valor será sacado?: R$'))

# Variável para armazenar o valor total que ainda precisa ser sacado
total = valor_sacado

# Define a primeira denominação de cédula como R$ 50
cedula = 50

# Variável para armazenar o número total de cédulas de cada denominação
total_cedulas = 0

# Loop principal para calcular as cédulas necessárias
while True:
    # Verifica se o valor total ainda é maior ou igual à cédula atual
    if total >= cedula:
        # Subtrai o valor da cédula atual do total
        total -= cedula
        # Incrementa o contador de cédulas correspondente
        total_cedulas += 1
    else:
        # Se o valor total for menor que a cédula atual
        if total_cedulas > 0:
            # Imprime quantas cédulas daquela denominação foram dispensadas
            print(f'Total de {total_cedulas} cédulas de R${cedula}')
        # Atualiza a denominação da cédula para a próxima menor
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        # Reinicia o contador de cédulas
        total_cedulas = 0
        # Verifica se todo o valor foi dispensado, encerrando o loop se sim
        if total == 0:
            break

# Imprime uma mensagem de despedida
print('=' * 30)
print('Volte sempre ao BANCO DEV! Tenha um bom dia!')
