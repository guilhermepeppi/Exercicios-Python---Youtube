# Faça um programa que leia nome
# e peso de várias pessoas, guardando tudo numa lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagam com as pessoas mais pesadas.
# C) Uma listagam com as pessoas mais leves.

# Lista para armazenar as pessoas
lista_pessoas = []
# Lista para armazenar as pessoas mais pesadas
pessoas_pesadas = []
# Lista para armazenar as pessoas mais leves
pessoas_leves = []
# Variáveis para armazenar o maior e o menor peso
maior_peso = menor_peso = 0

# Loop para coletar informações sobre as pessoas
while True:
    # Pede o nome e o peso da pessoa
    nome = input('Nome: ')
    peso = float(input('Peso (kg): '))

    # Se for a primeira pessoa inserida, define o maior e o menor peso
    if len(lista_pessoas) == 0:
        maior_peso = menor_peso = peso
    else:
        # Atualiza o maior e o menor peso, se necessário
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

    # Adiciona os dados da pessoa à lista
    lista_pessoas.append({'nome': nome, 'peso': peso})

    # Pergunta se deseja adicionar mais pessoas
    escolha = input('Quer continuar? [S/N]: ').strip().lower()
    if escolha != 's':
        break

# Itera sobre todas as pessoas na lista para encontrar as mais pesadas e as mais leves
for pessoa in lista_pessoas:
    if pessoa['peso'] == maior_peso:
        pessoas_pesadas.append(pessoa)
    elif pessoa['peso'] == menor_peso:
        pessoas_leves.append(pessoa)

# Conta quantas pessoas foram cadastradas
quantidade_pessoas = len(lista_pessoas)

# Exibe os resultados
print(f'A) Quantidade de pessoas cadastradas: {quantidade_pessoas}')
print('B) Pessoas mais pesadas:')
for pessoa in pessoas_pesadas:
    print(f"Nome: {pessoa['nome']}, Peso: {pessoa['peso']} kg")
print('C) Pessoas mais leves:')
for pessoa in pessoas_leves:
    print(f"Nome: {pessoa['nome']}, Peso: {pessoa['peso']} kg")
