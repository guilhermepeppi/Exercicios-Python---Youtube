# Faça um programa que leia um número inteiro e diga
# se se é ou não um número primo.

def is_prime(num):
    # Verifica se o número é menor que 2, pois números menores que 2 não são primos
    if num < 2:
        return False
    # Caso especial: o número 2 é primo
    if num == 2:
        return True
    # Verifica se o número é par diferente de 2, pois nenhum número par além de 2 é primo
    if num % 2 == 0:
        return False
    # Itera de 3 até a raiz quadrada do número, verificando se há algum divisor além de 1 e do próprio número
    # A iteração é feita apenas nos números ímpares, pois os pares já foram tratados
    # Cria um iterável que começa em 3 (pois já verificamos divisibilidade por 2) e vai
    # até a raiz quadrada de num (arredondada para cima) com um passo de 2.
    # Isso garante que apenas números ímpares sejam testados,
    # pois sabemos que nenhum número par além de 2 é primo.
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    # Se nenhum divisor além de 1 e do próprio número for encontrado, então o número é primo
    return True


try:
    # Solicita ao usuário que insira um número inteiro
    num = int(input("Digite um número inteiro: "))
    # Verifica se o número é primo utilizando a função is_prime e exibe o resultado
    if is_prime(num):
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
except ValueError:
    # Trata o erro caso a entrada não seja um número inteiro
    print("Entrada inválida. Por favor, digite um número inteiro.")
