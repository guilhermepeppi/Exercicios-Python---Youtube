# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

from Exercicio108 import moeda

preco = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é {moeda.dobro(preco):.2f}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10):.2f}')
print(f'Diminuindo 10%, temos {moeda.diminuir(preco, 10):.2f}')
