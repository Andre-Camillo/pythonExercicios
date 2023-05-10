palavras = ('aprender', 'programar', 'liguagem', 'python', 'praticar', 'trabalhar', 'mercado', 'programador')
for c in palavras:
    print(f'\nNA PALAVRA \033[1;36m{c.upper()}\033[m TEMOS: ',end='')
    for l in c:
        if l in 'aeiou':
            print(f'{l}', end='')

