tot = []
par = []
imp = []
for v in range(1, 8):
    val = int(input(f'DIGITE O {v}º VALOR: '))
    if val % 2 == 0:
        par.append(val)
    else:
        imp.append(val)
    tot.append(sorted(par))
    tot.append(sorted(imp))
#for c in tot:
#    print()
print(f'Números pares: {par}', end=' ')
print(f'\nNúmeros ímpares: {imp}', end=' ')

