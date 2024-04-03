# Crie um módulo chamado moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# ---
# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

def aumentar(preco=0, taxa=0):
    resultado = preco + (preco * taxa / 100)
    return resultado


def diminuir(preco=0, taxa=0):
    resultado = preco - (preco * taxa / 100)
    return resultado


def dobro(preco=0):
    resultado = preco * 2
    return resultado


def metade(preco=0):
    resultado = preco / 2
    return resultado


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco}'.replace('.', ',')
