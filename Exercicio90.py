# Faça um programa que leia nome e média da um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dados = {}

nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

situacao = "Aprovado" if media >= 7 else "Reprovado"

dados["nome"] = nome
dados["media"] = media
dados["situacao"] = situacao

print("\nDados do aluno:")
for chave, valor in dados.items():
    print(f"{chave.capitalize()}: {valor}")
