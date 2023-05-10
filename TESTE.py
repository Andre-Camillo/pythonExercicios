<<<<<<< HEAD
lanche = ['hamberger', 'suco', 'pizza', 'pudim']
print('')
for c in lanche:
    print(f"{c}", end=' ')
lanche[3] = "torta"
print(f'\n\n{lanche}')
lanche[0] = 'carro'
print(f'\n{lanche}')
lanche.append('cookie')
print(f'\n{lanche}')
lanche[4] = 'bolacha'
print(f'\n{lanche}')
lanche.insert(0, 'refri')
print(f'\n{lanche}')
=======
palavras = ('aprender', 'programar', 'liguagem', 'python', 'praticar', 'trabalhar', 'mercado', 'programador')
for c in palavras:
    print(f'\nNA PALAVRA \033[1;36m{c.upper()}\033[m TEMOS: ',end='')
    for l in c:
        if l in 'aeiou':
            print(f'{l}', end='')
>>>>>>> bed5330a91b65e2c97e9915a6500bc74d30f7ce9

