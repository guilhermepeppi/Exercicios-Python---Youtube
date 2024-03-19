# Cria um programa que vai ler vários números e colocar em uma listo.
# Depois disso, crie duas listas extras que vão conter openas os volores
# pares e os voloras impores digitados respectivamente.
# No final, mostre o conteudo dos tres listas geradas.

# Lista para armazenar os valores inseridos pelo usuário
valores = []
lista_pares = []
lista_impares = []

while True:
    try:
        valor = int(input(f"Digite o {len(valores) + 1}º valor: "))
        valores.append(valor)
        if valor % 2 == 0:
            lista_pares.append(valor)
        else:
            lista_impares.append(valor)
    except ValueError:
        print('Digite apenas números inteiros. ', end='')
        continue
    else:
        continuar = input("Deseja continuar? (S/N): ").strip().lower()[0]
        if continuar.lower() == 'n':
            break

print("Lista completa:", valores)
print("Lista de pares:", sorted(lista_pares))
print("Lista de ímpares:", sorted(lista_impares))
