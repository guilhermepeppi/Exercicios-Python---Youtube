# Adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas
# pelas funções que já temos no módulo criado até aqui.
# ---
# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

def aumentar(preco=0, taxa=0, formato=False):
    resultado = preco + (preco * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def diminuir(preco=0, taxa=0, formato=False):
    resultado = preco - (preco * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def dobro(preco=0, formato=False):
    resultado = preco * 2
    return resultado if not formato else moeda(resultado)


def metade(preco=0, formato=False):
    resultado = preco / 2
    return resultado if not formato else moeda(resultado)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxa=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Aumentando {taxaa}%, temos: \t{aumentar(preco, taxaa, True)}')
    print(f'Diminuindo {taxa}%, temos: \t{diminuir(preco, taxa, True)}')
    print('-' * 30)
