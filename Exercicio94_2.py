# Crie um programa que leia nome, sexo e idade de várias pessoas.
# guardando os dados de cada pessoa
# em um dicionário e todos os dicionários
# em uma lista. No final, mostre
# A) Quantas pessoas cadastradas
# B) A média de idade.
# C) Uma lista com mulheres.
# D) Uma lista com idade acima da média.

# Lista para armazenar os dicionários de pessoas
lista_pessoas = []

while True:
    # Lendo os dados da pessoa
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    sexo = input("Digite o sexo da pessoa (M/F): ")
    idade = int(input("Digite a idade da pessoa: "))

    # Criando o dicionário da pessoa
    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}

    # Adicionando o dicionário à lista de pessoas
    lista_pessoas.append(pessoa)

# A) Quantidade de pessoas cadastradas
total_pessoas = len(lista_pessoas)
print(f"A) Total de pessoas cadastradas: {total_pessoas}")

# B) Média de idade
total_idade = sum(pessoa['idade'] for pessoa in lista_pessoas)
media_idade = total_idade / total_pessoas if total_pessoas > 0 else 0
print(f"B) Média de idade: {media_idade:.2f}")

# C) Lista de mulheres
mulheres = [pessoa['nome'] for pessoa in lista_pessoas if pessoa['sexo'].upper() == 'F']
print("C) Lista de mulheres:", mulheres)

# D) Lista de pessoas com idade acima da média
acima_da_media = [pessoa['nome'] for pessoa in lista_pessoas if pessoa['idade'] > media_idade]
print("D) Lista de pessoas com idade acima da média:", acima_da_media)
