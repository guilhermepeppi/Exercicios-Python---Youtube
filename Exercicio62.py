# Melhora o DESAFIo 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('=' * 15)
numero = int(input('Primeiro termo: '))
pa = int(input('Razão da PA: '))
contador = 10

while True:
    while contador > 0:
        print(f'{numero}', end=' - ')
        numero += pa
        contador -= 1
    print('PAUSA')

    pa_continuacao = int(input('Quantos termos você quer mostrar a mais?: '))
    if pa_continuacao == 0:
        break
    contador = pa_continuacao

print('FIM')
