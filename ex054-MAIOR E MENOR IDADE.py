print('MAIOR E MENOR IDADE')
from datetime import date
color = {'clear': '\033[m', 'red': '\033[31m', 'green': '\033[31m', 'cyan': '\033[31m' }
ano_atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 5):
    ano_nasc = int(input('Informe o ano de nascimento: '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('MAIORES DE IDADE: {}.'.format(maior))
print('MAIORES DE IDADE: {}.'.format(menor))

