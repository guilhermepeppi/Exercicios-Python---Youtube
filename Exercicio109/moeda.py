'''
GitHub Copilot
O código fornecido contém uma série de funções relacionadas a manipulação de valores monetários. Vamos analisar cada uma delas:

A função aumentar(preco=0, taxa=0, formato=False) recebe dois parâmetros: preco (valor do preço) e taxa (porcentagem de aumento). O parâmetro opcional formato indica se o valor retornado será formatado como uma moeda. A função calcula o valor resultante após o aumento e retorna esse valor. Se o parâmetro formato for True, a função chama a função moeda() para formatar o valor antes de retorná-lo.

A função diminuir(preco=0, taxa=0, formato=False) é semelhante à função aumentar(), mas calcula o valor resultante após a redução com base na taxa fornecida.

A função dobro(preco=0, formato=False) recebe o parâmetro preco e retorna o dobro desse valor. O parâmetro opcional formato indica se o valor retornado será formatado como uma moeda. Se formato for True, a função chama a função moeda() para formatar o valor antes de retorná-lo.

A função metade(preco=0, formato=False) é semelhante à função dobro(), mas retorna a metade do valor fornecido.

A função moeda(preco=0, moeda='R$') recebe o parâmetro preco e opcionalmente moeda (que é definido como 'R$' por padrão). Essa função formata o valor monetário fornecido, adicionando o símbolo da moeda e exibindo-o com duas casas decimais. Por exemplo, se o valor for 10.5, a função retornará 'R$10,50'.

Essas funções foram modificadas a partir de um desafio anterior para aceitar um parâmetro adicional chamado formato, que indica se o valor retornado deve ser formatado como uma moeda. Se formato for True, as funções chamam a função moeda() para formatar o valor antes de retorná-lo. Isso permite que o usuário escolha se deseja ou não que o valor seja formatado como uma moeda.
'''

# Modifique as funções que form criadas no desafio 107 para que
# elas aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
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


