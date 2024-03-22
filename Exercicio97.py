# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# ЕX:
# escreva('Olá, Mundo!')
# Saida:
# ˜˜˜˜˜˜˜˜˜˜˜
# Olá, Mundo!
# ˜˜˜˜˜˜˜˜˜˜˜

def escreva(txt):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('~' * tamanho)


texto = str(input('Digite o texto: '))
escreva(texto)
