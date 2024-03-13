# Rafaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilatero: todos os lados iguais
# - Isosceles: dois lados iguais
# - Escaleno - todos os lados diferentes


print()
print('ニーニーニーニーニーニーニ')
print('Analisador de Triângulos')
print('ニーニーニーニーニーニーニ')
print()

primeiro_seguimento = float(input('Primeiro segmento: '))
segundo_segmento = float(input('Segundo segmento: '))
terceiro_segmento = float(input('Terceiro segmento: '))

if (
    primeiro_seguimento < segundo_segmento + terceiro_segmento and
    segundo_segmento < primeiro_seguimento + terceiro_segmento and
    terceiro_segmento < primeiro_seguimento + segundo_segmento
):
    print('Os segmentos acima PODEM FORMAR triângulo ', end='')
    if primeiro_seguimento == segundo_segmento == terceiro_segmento:
        print('EQUILÁTERO')
    elif primeiro_seguimento != segundo_segmento != terceiro_segmento != primeiro_seguimento:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
