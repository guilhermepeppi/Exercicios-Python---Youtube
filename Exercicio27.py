# Faça um programa que leia o nome complato de uma pessoa. mostrando em seguida o primairo e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = input('Digite um nome: ').strip().split()

print(f'Primeiro = {nome[0]}')
print(f'Ultimo = {nome[-1]}')
