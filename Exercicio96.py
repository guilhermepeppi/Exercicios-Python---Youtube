# Faça um programa que tenha uma Função chamada area,
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a árca do terreno.

def area(largura, comprimento):
    area_calculada = largura * comprimento
    print(f'A area calculada: {area_calculada}m²')


largura = float(input('Largura (em metros): '))
comprimento = float(input('Digite o comprimento (em metros): '))
area(largura, comprimento)
