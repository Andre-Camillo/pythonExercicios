num = list()
cont = ''
while True:
    n = int(input('DIGITE UM VALOR: '))
    if n not in num:
        num.append(n)
        print('\033[32mVALOR ADICIONADO COMSUCESSO\033[m')
    else:
        print('\033[1:31mVALOR DUPLICADO, NÃO ADICIONADO\033[m')
    r = str(input('DESEJA CONTINUAR? [S] ou [N]: '))

    while r not in 'SsNn':
        r = str(input('VOCÊ DEVE DIGITAR [S] ou [N]: '))
    if r in 'Nn':
        break
print(f'OS NÚMEROS DIGITADOR FORAM: ', end='')
for c in sorted(num):
    print(f'{c}', end=' ')

#Ou

print()
print(f'OS NÚMEROS DIGITADOR FORAM: ', end='')
num.sort()
for c in num:
    print(f'{c}', end=' ')

