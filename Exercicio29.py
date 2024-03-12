# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizando que ela foi multado.
# A multa vai custar R$7.00 por cada km acima do limite.

velocidade = int(input('Digite a velocidade do carro: '))
multa_valor = 0

if velocidade > 80:
    print('Carro multado')
    multa_valor = (velocidade-80) * 7
    print(f'Valor da multa R${multa_valor:.2f}')
else:
    print('Carro não multado')
