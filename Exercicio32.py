# Faça um programa que leia um ano qualquer o mostra sa cic é BISSEXTO.

from datetime import date

ano = int(input('Digite o ano para analisar. 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('0 ano {} é BISSEXTO'.format(ano))
else:
    print('0 ano {} NÃO é BISSEXTO'.format(ano))
