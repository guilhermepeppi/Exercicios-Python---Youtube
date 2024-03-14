# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
# de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles

from time import sleep

tempo = 10

while tempo >= 0:
    print(tempo)
    sleep(1)
    tempo -= 1
