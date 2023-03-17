rint('*' * 26)
print('* SEQUÊNCIA DE FIBONACCI *')
print('*' * 26)
num = int(input('INFORME A QUANTIDADE DE TERMOS: '))
t1 = 1
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(' - {}' .format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - Fim...')
