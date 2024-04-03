# Crie um módulo chamado moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(preco, taxa):
    resultado = preco + (preco * taxa / 100)
    return resultado


def diminuir(preco, taxa):
    resultado = preco - (preco * taxa / 100)
    return resultado


def dobro(preco):
    resultado = preco * 2
    return resultado


def metade(preco):
    resultado = preco / 2
    return resultado
