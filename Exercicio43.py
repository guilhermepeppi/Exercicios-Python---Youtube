# Dasenvolva uma lógica que leia o peso e a altura de uma pessoa.
# calcula seu IMC e mostre seu status, de acordo com a tabala abaixo:
# - Abaixo da 18.5: Abaixo do peso
# - Entre 18.5 a 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima da 40: Obesidade mórbida


peso = float(input('Qual é seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (m): '))

calculo = peso / (altura ** 2)
print(f'IMC: {calculo:.2f}')

if calculo < 18.5:
    print('Abaixo do peso')
elif calculo >= 18.5 and calculo <= 24.9:
    print('Peso ideal')
elif calculo >= 25 and calculo <= 29.9:
    print('Sobrepeso')
elif calculo >= 30 and calculo <= 39.9:
    print('Obesidade')
else:
    print('Obesidade mórbida')
