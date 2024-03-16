# Crie um programa que leia dois valoras a mostre um menu como o ao lado na tala:
# Seu programa devará realizar a operação solicitada em cada caso.


primeiro_valor = float(input('Primeiro valor: '))
segundo_valor = float(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('>>>> Qual é a sua opção? '))

    if opcao == 1:
        resultado = primeiro_valor + segundo_valor
        print(f'A soma entre {primeiro_valor} e {segundo_valor} é {resultado}')
    elif opcao == 2:
        resultado = primeiro_valor * segundo_valor
        print(f'O produto entre {primeiro_valor} e {segundo_valor} é {resultado}')
    elif opcao == 3:
        maior = max(primeiro_valor, segundo_valor)
        print(f'O maior número entre {primeiro_valor} e {segundo_valor} é {maior}')
    elif opcao == 4:
        primeiro_valor = float(input('Primeiro valor: '))
        segundo_valor = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')

print('Programa encerrado.')
