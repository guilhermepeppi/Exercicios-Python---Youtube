# Desenvolva um programa que leia o nome, idade e sexo de 4 passoas. No Final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

media_idade = 0
idade_homem_mais_velho = float('-inf')
homem_mais_velho = ''
quantidade_mulheres = 0

for pessoas in range(1, 5):
    print(f'-----{pessoas}ª PESSOA-----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

    media_idade += idade

    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        quantidade_mulheres += 1

media_idade /= 4

print(f'A média de idade é {media_idade}')
print(f'O homem mais velho é: {homem_mais_velho}')
print(f'A quantidade de mulheres com menos de 20 anos é: {quantidade_mulheres}')
