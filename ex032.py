from datetime import date
print('INFORMA SE O ANO É BISSEXTO')
ano = int(input('''Coloque "0" para analizar o ano atual ou
Digite o ano para saber se ele é Bissexto: '''))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} \033[1;32mÉ\033[m Bissexto.'.format(ano))
else:
    print('O ano de {} \033[1;31mNÃO É\033[m Bissexto.'.format(ano))