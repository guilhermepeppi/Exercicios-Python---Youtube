# Crie um programa que leia nome, sexo e idade de várias pessoas.
# guardando os dados de cada pessoa
# em um dicionário e todos os dicionários
# em uma lista. No final, mostre
# A) Quantas pessoas cadastradas
# B) A média de idade.
# C) Uma lista com mulheres.
# D) Uma lista com idade acima da média.

galera = list()
pessoa = dict()
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resposta in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resposta == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'B) A média de idade é de {média:.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p["idade"] >= média:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
print('<< ENCERRADO >>')
