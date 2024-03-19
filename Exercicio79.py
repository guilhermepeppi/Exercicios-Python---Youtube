# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastra-los em uma lista. Caso o número já exista
# lá dantro ele não será adicionado. No Final, será exibido
# todos os valores únicos digitados, em ordem crescente.

valores = []

while True:
    try:
        valor = int(input('Digite um valor: '))
        valores.append(valor)
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha == 'S':
            continue
        else:
            break

    except ValueError:
        print("Erro: Digite apenas valores inteiros.")

# Converte a lista para um conjunto (set, que não contém duplicados)
# e depois converte de volta para uma lista e coloca em ordem
valores_sem_duplicatas = list(sorted(set(valores)))


print(f'Você digitou os valores: {valores_sem_duplicatas}')
