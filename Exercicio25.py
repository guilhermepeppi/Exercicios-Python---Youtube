# Programa que verifique se existe a palavra Silva no nome da pessoa

nome = input('Digite seu nome: ').strip().title()

if 'Silva' in nome:
    print('Há Silva no teu nome')
else:
    print('Não tem Silva no teu nome')
