# # A confederação Nacional de Natação preciso de um programa que leia o ano de nascimento
# de um atlata a mostra sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SeNIOR
# - Acima: MASTER

import datetime

ano_nascimento = int(input('Digite o ano de nascimento: '))

idade = datetime.date.today().year - ano_nascimento

print(idade)

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
