# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastra-os (com idade) em um dicionário se por
# acaso a CTPS for diferente da ZER0, o dicionfrio receberá
# também o ano da contratação e o salário. Calcule e acrescente
# além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

pessoa = {}

nome = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
carteira_trabalho = input("Número da carteira de trabalho (ou 0 se não tiver): ")

pessoa['nome'] = nome
pessoa['idade'] = datetime.now().year - ano_nascimento

if carteira_trabalho != '0':
    ano_contratacao = int(input("Ano de contratação: "))
    salario = float(input("Salário: "))
    idade_contratacao = ano_contratacao - ano_nascimento
    anos_aposentadoria = 65 - idade_contratacao
    pessoa['ano_contratacao'] = ano_contratacao
    pessoa['salario'] = salario
    pessoa['anos_aposentadoria'] = max(0, anos_aposentadoria)

print("\nDados da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")
