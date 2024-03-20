# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.

# Lista composta para armazenar os dados dos alunos
alunos = []

# Loop para ler nome e notas de vários alunos
while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    # Calcula a média das notas do aluno
    media = (nota1 + nota2) / 2

    # Adiciona os dados do aluno à lista composta
    alunos.append([nome, nota1, nota2, media])

    continuar = input("Deseja cadastrar outro aluno? (S/N): ").strip().upper()
    if continuar != 'S':
        break

# Exibindo o boletim com a média de cada aluno
print("\nBoletim:")
for aluno in alunos:
    print(f"Nome: {aluno[0]}, Média: {aluno[3]}")

# Mostrando as notas de cada aluno individualmente
while True:
    opcao = input("\nDeseja ver as notas de algum aluno? (S/N): ").strip().upper()
    if opcao != 'S':
        break
    nome_aluno = input("Digite o nome do aluno: ")
    for aluno in alunos:
        if aluno[0] == nome_aluno:
            print(f"Notas de {nome_aluno}: {aluno[1]} e {aluno[2]}")
            break
    else:
        print(f"Aluno {nome_aluno} não encontrado.")
