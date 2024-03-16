# Faça um programa que leia o sexo de uma passoa, mas só aceita os valores 'M' ou 'F'.
# Caso esteja arrado. peça a digitação novamente até ter um valor correto.

# removendo espaços em branco extras, convertendo todos os caracteres para maiúsculas
# e selecionando apenas o primeiro caractere.
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso')
