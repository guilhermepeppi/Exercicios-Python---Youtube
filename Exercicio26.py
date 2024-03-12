# Faça um programa que Icia uma frase pala teclado e mostra:
# Quantas vazas aparece a letra "A".
# Em que posição ala aparece a primeira vez.
# Em que posição ela aparece a última

frase = input('Digite uma frase: ').strip().upper()  # Amanda ama Pedro

print(f'A letra A aparece {frase.count("A")} vezes na frase.')

print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')

print(f'A última letra A apareceu na posição {frase.rfind("A")+1}')
