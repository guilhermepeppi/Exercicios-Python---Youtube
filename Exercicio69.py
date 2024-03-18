# Cric um programa que leia a idade e o sexo de várias passoas.
# A cada pessoas cadastrada, o programa devera porguntar se o usuario quer
# ou não continuar. No final, mostra:
# A) quantas passogs tam mais da 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tom menos da 20 anos.

print('=' * 25)
print('CADASTRO DE PESSOAS')
print('=' * 25)

total_maior_idade = 0
total_sexo_masculino = 0
total_mulheres_idade = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MmFf':
        print('Dado incorreto.')
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        total_maior_idade += 1

    if sexo == 'M':
        total_sexo_masculino += 1

    if sexo == 'F' and idade < 20:
        total_mulheres_idade += 1

    print()
    print('~' * 25)
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('~' * 25)
    print()
    while escolha not in 'SsNn':
        print()
        print('~' * 25)
        print('Valor incorreto.')
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print()
        print('~' * 25)

    if escolha == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {total_maior_idade}')
print(f'Total de homens cadastrados: {total_sexo_masculino}')
print(f'Total de mulheres com mais de 20 anos: {total_mulheres_idade}')
