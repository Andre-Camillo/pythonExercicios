print('P. A.')
prim = int(input('INFORME O 1° TERMO: '))
raz = int(input('INFORME A RAZÃO: '))
decimo = prim + (11 - 1) * raz
for c in range(prim, decimo, raz):
    print(c, '- ',end=' ')
print('FIM')

