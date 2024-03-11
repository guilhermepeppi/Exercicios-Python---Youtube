import random

primeiro_aluno = str(input('Primeiro aluno: '))
segundo_aluno = str(input('Segundo aluno: '))
terceiro_aluno = str(input('Terceiro aluno: '))
quarto_aluno = str(input('Quarto aluno: '))

lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]

escolhido = random.choice(lista)

print(f'O aluno escolhido foi {escolhido}')
