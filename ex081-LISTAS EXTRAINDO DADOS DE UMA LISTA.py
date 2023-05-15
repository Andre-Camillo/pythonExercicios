num = []
seguir = ''
while True:
    num.append(int(input(f'INFORME UM VALOR: ')))
    seguir = str(input('DESEJA CONTINUAR? [S] ou [N]: '))
    if seguir in 'Nn':
        break
    while seguir not in 'SsNn':
        seguir = str(input('VOCÊ DEVE DIGITAR [S] ou [N]: ')).upper()
print(f'\033[1mNUMEROS DIGITADOS:\033[m ', end='')
for c in num:
    print(f'\033[1m{c}\033[m', end=' ')
print(f'\033[1m\nTOTAL DE NÚMEROS DIGITADOS: {len(num)}\033[m.')
print(f'\033[1mINVERTENDO A ORDEM: \033[m', end='')
num.sort(reverse=True)
for l in num:
    print(f'\033[1m{l}\033[m', end=' ')
if 5 in num:
    print(f'\033[1m\nO VALOR "5" FOI DIGITARO E ENCONTRA-SE NA POSIÇÃO Nº {num.index(5) + 1}\033[m')
else:
    print('\033[1m\nO VALOR "5" NÃO FOI DIGITADO\033[m')



