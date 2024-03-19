# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar. para cada palaura, quais sao as suas vogais.

# Tupla com as palavras
palavras = (
    "girafa",
    "computador",
    "montanha",
    "elefante",
    "avião",
    "bicicleta",
    "ocidental",
    "banana",
    "velocidade",
    "floresta",
    "piano",
    "escola",
    "fotografia",
    "sorvete",
    "amarelo"
)

# Iterar sobre cada palavra na tupla
for p in palavras:
    # Imprimir a palavra em maiúsculas
    print(f'\nNa palavra {p.upper()} temos ', end='')

    # Iterar sobre cada letra na palavra
    for letra in p:
        # Verificar se a letra é uma vogal (sem considerar acentos)
        if letra.lower() in 'aeiou':
            # Se for uma vogal, imprimir a vogal
            print(letra, end=' ')
