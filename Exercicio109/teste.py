import moeda

# Solicita ao usuário que digite o preço e converte para float
preco = float(input('Digite o preço: R$'))

# Imprime a metade do preço utilizando a função 'metade' do módulo 'moeda'
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')

# Imprime o dobro do preço utilizando a função 'dobro' do módulo 'moeda'
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')

# Imprime o preço aumentado em 10% utilizando a função 'aumentar' do módulo 'moeda'
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')

# Imprime o preço diminuído em 10% utilizando a função 'diminuir' do módulo 'moeda'
print(f'Diminuindo 10%, temos {moeda.diminuir(preco, 10, True)}')
