import math  # Podendo usar - from math import hypot

print('Forma 1')
cateto_oposto = float(input('Comprimento do cateto oposto: '))  # 3.5
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))  # 4.75

resultado_1 = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print(f'A hipotenusa vai medir {resultado_1:.2f}')


print()
print('Forma 2')
cateto_oposto = float(input('Comprimento do cateto oposto: '))  # 3.5
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))  # 4.75

resultado_2 = math.hypot(cateto_oposto, cateto_adjacente)  # se usar o segundo método de import, apagar math

print(f'A hipotenusa vai medir {resultado_2:.2f}')
