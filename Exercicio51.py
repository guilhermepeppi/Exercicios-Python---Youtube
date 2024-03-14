# Dasenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros
# termos dassa prograssio.

print('-' * 20)
print('10 TERMOS DE UMA PA')
print('-' * 20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(10):
    numero = primeiro_termo + razao * i
    print(f'{numero}', end=' -> ')

print('ACABOU!')
