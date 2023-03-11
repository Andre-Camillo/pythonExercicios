print('DESCOBRE SE É NÚMERO PRIMO')
num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print('\033[1;32m{}\033[m'.format(c), end=' ')
    else:
        print('\033[1;31m{}\033[m'.format(c), end=' ')
if cont == 2:
    print('\nO NÚMERO "\033[1;32m{}\033[m" \033[1;32mÉ PRIMO.\033[m.'.format(num))
else:
    print('\nO NÚMERO "\033[1;31m{}\033[m" \033[1;31mNÃO É PRIMO.\033[m.'.format(num))
