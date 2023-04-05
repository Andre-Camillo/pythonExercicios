print('SEPARA O PRIMEIRO E O ÚLTIMO NOME.')
nome = str(input('Digite seu nome completo: ')).strip().split()
print('''Olá {}!
Seu 1° é: {}.
Seu último nome é: {}.'''.format(' '.join(nome).title(), nome[0].title(), nome[len(nome)-1].title()))


