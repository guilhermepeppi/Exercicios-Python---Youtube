# O Carro custa R$60,00 por dia e R$0,15 por km rodado

dias = int(input('Quantos dias alugados? '))  # 8
km_rodados = float(input('Quantos Km rodados? '))  # 720

total_a_pagar = (dias * 60) + (km_rodados * 0.15)

print(f'O total a pagar é de R${total_a_pagar:.2f}')
