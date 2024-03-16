# Rafaça o DESAFIO 051, lendo o primeiro termo a a razão de uma PA,
# mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print('Gerador de PA')
print('=' * 15)
numero = int(input('Primeiro termo: '))
pa = int(input('Razão da PA: '))

contador = 10

while contador > 0:
    print(f'{numero}', end=' - ')
    numero += pa
    contador -= 1

print('FIM')
