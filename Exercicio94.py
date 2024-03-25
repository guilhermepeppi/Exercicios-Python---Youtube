# Crie um programa que leia nome, sexo e idade de várias pessoas.
# guardando os dados de cada pessoa
# em um dicionário e todos os dicionários
# em uma lista. No final, mostre
# A) Quantas pessoas cadastradas
# B) A média de idade.
# C) Uma lista com mulheres.
# D) Uma lista com idade acima da média.

# Inicializa uma lista vazia chamada "galera" para armazenar os dicionários de pessoa.
galera = list()
# Inicializa um dicionário vazio chamado "pessoa" para armazenar os dados de cada pessoa.
pessoa = dict()
soma = média = 0

# Loop principal para continuar a coleta de dados das pessoas.
while True:
    # Limpa o dicionário "pessoa" para armazenar os dados de uma nova pessoa.
    pessoa.clear()
    # Solicita ao usuário que insira o nome da pessoa e armazena no dicionário "pessoa".
    pessoa['nome'] = str(input('Nome: '))
    # Loop para garantir que o sexo inserido seja válido (M ou F) e armazena no dicionário "pessoa".
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    # Solicita ao usuário que insira a idade da pessoa e armazena no dicionário "pessoa".
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    # Adiciona uma cópia do dicionário "pessoa" à lista "galera".
    galera.append(pessoa.copy())
    # Loop para verificar se o usuário deseja continuar adicionando pessoas.
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resposta in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    # Se a resposta for 'N', o loop principal é interrompido e a execução do programa é encerrada.
    if resposta == 'N':
        break

# Imprime uma linha de separação.
print('-=' * 30)
# Imprime o último dicionário "pessoa" (que não foi limpo no final do loop).
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
    if p["indade"] >= média:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
print('<< ENCERRADO >>')
