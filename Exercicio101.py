# Cria um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa.
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano_nascimento):
    from datetime import datetime
    idade = datetime.now().year - ano_nascimento
    if idade < 16:
        return f"Com {idade} anos, o voto é NEGADO"
    elif idade >= 18 and idade < 70:
        return f"Com {idade} anos, o voto é OBRIGATÓRIO"
    else:
        return f"Com {idade} anos, o voto é OPCIONAL"


ano_nascimento = int(input('Ano de nascimento: '))
print(voto(ano_nascimento))
