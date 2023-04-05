print('P.A. COM LAÇO WH')
prim = int(input('INFORME O 1° TERMO: '))
raz = int(input('INFORME A RAZÃO: '))
termo = prim
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += raz
    cont += 1
print('FIM')
