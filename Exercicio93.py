# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionario.
# incluindo o total de gols feitos durante o campeonato.

jogadores = {}
gols_por_partida = []

nome = input('Nome: ')
numero_partidas = int(input('Número de partidas: '))

for partida in range(numero_partidas):
    gols = int(input(f'Gols na partida {partida + 1}: '))
    gols_por_partida.append(gols)

jogadores['nome'] = nome
jogadores['gols_por_partida'] = gols_por_partida
jogadores['total_gols'] = sum(gols_por_partida)

print("\nDados do jogador:")
print(f'Nome: {jogadores["nome"]}')
print(f'Número de partidas: {numero_partidas}')
print(f'Gols por partida: {jogadores["gols_por_partida"]}')
print(f'Total de gols: {jogadores["total_gols"]}')
