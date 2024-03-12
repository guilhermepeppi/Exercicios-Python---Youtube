# Dasenvolva um programa qua laia o comprimanto de três retas
# e diga ao usuário se elas podam ou
# neo Formar um triangulo.

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
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
