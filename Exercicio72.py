# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# a mostrá-lo por antenso.

# Desafio: incrementar o código para perguntar se quer continuar

numeros_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {numeros_extenso[numero]}.')
    else:
        print('Número fora da faixa permitida.')
        continue
    escolha = input('Quer continuar? [S/N]: ').strip().upper()
    if escolha != 'S':
        break
