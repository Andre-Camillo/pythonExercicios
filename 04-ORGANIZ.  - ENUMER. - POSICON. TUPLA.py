# 1ª FORMA
lanche = ('HAMBURGER', 'SUCO', 'PIZZA', 'PUDIM', 'BATATA FRITA')
for pos, cont in enumerate(lanche):
    print(f'{pos + 1}º CONSUMIREI {cont}. ')

# 2ª FORMA
for cont in range(0, len(lanche)): # ou (len(lanche))
    print(f'{cont + 1}º CONSUMIREI {lanche[cont]}.')

# 3ª FORMA
for cont in range(0, len(lanche)): # ou (len(lanche))
    print(f'{cont + 1}º CONSUMIREI {sorted(lanche)[cont]}.')

