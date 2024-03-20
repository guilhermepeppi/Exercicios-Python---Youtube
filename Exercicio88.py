# Faça um programa que ajude um jogador da MEGA SENA
# a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo,
# cadastrando tudo aemm uma lista composta.

from random import randint

jogos = []

print('-' * 30)
print(f'{"MEGA SENA":^30}')
print('-' * 30)


total_jogos = int(input('Total de jogos: '))
print()

# Gerando os jogos e adicionando à lista composta
for _ in range(total_jogos):
    jogo = []  # Inicia uma lista vazia para cada jogo
    while len(jogo) < 6:  # Garante que cada jogo tenha 6 números únicos
        numero = randint(1, 60)
        if numero not in jogo:  # Verifica se o número já foi sorteado
            jogo.append(numero)
    jogo.sort()  # Ordena os números do jogo em ordem crescente
    jogos.append(jogo)

# Exibindo os jogos
print("Palpites da MEGA SENA:")
for jogo in jogos:
    print(jogo)
