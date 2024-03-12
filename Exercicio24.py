# Programa que verifica se a cidade começa com SANTO

cidade = input('Digite sua cidade: ').strip()

print(cidade[:5].upper == 'SANTO')
