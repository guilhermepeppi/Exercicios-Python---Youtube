# Cria um programa que leia uma frase qualquer e diga
# se ela é um palindromo, desconsiderando os espaços.

frase = input('Digite uma frase: ')
frase_sem_espacos = frase.replace(' ', '').upper()

frase_invertida = frase_sem_espacos[::-1]

print(f"Frase original: {frase_sem_espacos}")
print(f"Frase invertida: {frase_invertida}")

if frase_sem_espacos == frase_invertida:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo.')
