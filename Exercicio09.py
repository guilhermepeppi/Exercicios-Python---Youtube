num = int(input('Digite um número para ver a tabuada: '))

valor = 1

print('-------------')

while valor <= 10:
    print(f'{num} x {valor} = {valor*num}')
    valor += 1

print('-------------')
