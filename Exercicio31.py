# Desenvolva um programa que pargunte a
# distância de uma viagem em Km. Calcula o preso da passagam,
# cobrando R$0.50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Digite a distancia da sua viagem: '))
valor = 0

if distancia <= 200:
    valor = distancia * 0.50
    print(f'Valor da viagem R${valor}')
else:
    valor = distancia * 0.45
    print(f'Valor da viagem R${valor}')
