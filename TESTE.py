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

