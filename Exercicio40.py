# Crie um programa que leia duas notas de um aluno e calcula sua média.
#  mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo da 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))

media = (nota_um + nota_dois) / 2

print(media)

if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
