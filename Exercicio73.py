# Crie uma tupla preanchida com os 20 primeiros colocados da Tabela do Campaonato Brasileiro de Futebol
# na ordem de colocação. Dapois mostre:
# A) Os 5 primeiros.
# B) Os últimos 4 colocados.
# C) Times am ordem alfabética.
# D1 Em qua posição está o time da Chapecoense.

times_brasileirao = ("Athletico Paranaense", "Atlético Goianiense", "Atlético Mineiro", "Bahia", "Ceará", "Chapecoense", "Corinthians", "Cuiabá", "Flamengo",
                     "Fluminense", "Fortaleza", "Grêmio", "Internacional", "Juventude", "Palmeiras", "Red Bull Bragantino", "Santos", "São Paulo", "Sport", "Vasco da Gama")


cinco_primeiros = times_brasileirao[:5]
quatro_ultimos = times_brasileirao[-4:]
times_ordenados = tuple(sorted(times_brasileirao))
posicao_chapecoense = times_brasileirao.index("Chapecoense") + 1

print('=' * 50)
print(f'Os 5 primeiros: {cinco_primeiros}.')
print('=' * 50)
print(f'Os 4 ultimos: {quatro_ultimos}.')
print('=' * 50)
print(f'Lista ordenada: {times_ordenados}.')
print('=' * 50)
print(f'A Chapecoense está na {posicao_chapecoense}ª posição ')
print('=' * 50)
