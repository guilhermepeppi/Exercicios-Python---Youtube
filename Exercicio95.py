# ----------EXERCICIO 95----------
# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
# incluindo um sistama da visualização de detalhes de aproveitamento do cada jogador.
# ----------EXERCICIO 93----------
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionario.
# incluindo o total de gols feitos durante o campeonato.

while True:
    jogadores = []

    while True:
        jogador = {}
        nome = input('Nome do jogador: ')
        if not nome:
            break
        numero_partidas = int(input('Número de partidas: '))

        gols_por_partida = []
        for partida in range(numero_partidas):
            gols = int(input(f'Gols na partida {partida + 1}: '))
            gols_por_partida.append(gols)

        jogador['nome'] = nome
        jogador['gols_por_partida'] = gols_por_partida
        jogador['total_gols'] = sum(gols_por_partida)

        jogadores.append(jogador)

    print("\nDados dos jogadores:")
    for jogador in jogadores:
        print("\n---")
        print(f'Nome: {jogador["nome"]}')
        print(f'Número de partidas: {len(jogador["gols_por_partida"])}')
        print(f'Gols por partida: {jogador["gols_por_partida"]}')
        print(f'Total de gols: {jogador["total_gols"]}')

    continuar = input("\nDeseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break
