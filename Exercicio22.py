nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

print(f'Seu nome em maiúsculas é {nome.upper()}')

print(f'Seu nome em minúsculas é {nome.lower()} ')

print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras')

nome_separado = nome.split()
print(f'Seu primeiro nome é {nome_separado[0]} e tem letras {nome.find(" ")}')
