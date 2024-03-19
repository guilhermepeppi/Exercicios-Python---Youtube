# Dasenvolva um programa que leia quatro valores
# pelo teclado a guarda-os em uma tupla. No final, mostre:
# A) Quantas vazas apareceu o valor 9.
# Bi Em que posição foi digitado o primairo valor 3.
# C) Quais foram os números pares.


# Ler os valores digitados pelo usuário
valores = []
for i in range(4):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

# Contar quantas vezes o valor 9 aparece
contagem_nove = valores.count(9)

# Encontrar a posição do primeiro valor 3
if 3 in valores:
    posicao_tres = valores.index(3) + 1  # Adiciona 1 para ajustar a posição (começando de 1)
else:
    posicao_tres = "O valor 3 não foi digitado."

# Encontrar os números pares
pares = [num for num in valores if num % 2 == 0]

# Mostrar os resultados
print(f"A) O valor 9 apareceu {contagem_nove} vezes.")
print(f"B) O primeiro valor 3 foi digitado na posição {posicao_tres}.")
print(f"C) Os números pares digitados foram: {pares}")
