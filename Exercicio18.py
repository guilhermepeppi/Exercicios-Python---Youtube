import math

angulo = float(input('Digite o ângulo que você deseja: '))  # 30

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))


print(f'Ângulo de {angulo} tem o SENO de {seno:.2f}')  # 0.50
print(f'Ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')  # 0.87
print(f'Ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')  # 0.58
