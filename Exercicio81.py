# Crie um programa que vai ler vários números e colocar em uma listo. Dapois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valoras, ordanada do forma decrescente.
# C) Se o valor 5 foi digitado e está ou nao na lista.


# Lista para armazenar os valores inseridos pelo usuário
valores = []
positivo = False

while True:
    try:
        valor = int(input(f"Digite o {len(valores) + 1}º valor: "))
        valores.append(valor)
        if valor == 5:
            positivo = True
    except ValueError:
        print('Digite apenas números inteiros. ', end='')
        continue
    else:
        continuar = input("Deseja continuar? (S/N): ").strip().lower()[0]
        if continuar.lower() == 'n':
            break


valores.sort(reverse=True)
print("Valores inseridos:", valores)
if positivo:
    print('O número 5 foi digitado')
else:
    print('O número 5 NÃO foi digitado')
