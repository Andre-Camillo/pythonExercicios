num = (int(input(f'DIGITE UM NÚMERO: ')), int(input(f'DIGITE OUTRO NÚMERO: '))
        , int(input(f'DIGITE MAIS UM NÚMERO: ')), int(input(f'DIGITE O ÚLTIMO NÚMERO: ')))
print(f'VOCÊ DIGITOU OS VALORES: {num}')
if 9 in num:
    print(f'O NÚMERO "9" APARECE {num.count(9)} VEZ(ES)')
else:
    print(f'O Nº "9" NÃO FOI DIGITADO.')
if 3 in num:
    print(f'O NÚMERO "3" APARECE NA POSIÇÃO DE Nº {num.index(3) + 1}.')
else:
    print(f'O Nº "3" NÃO FOI DIGITADO')
print('NÚMERO(S) PAR(ES) DIGITADO(S): ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='  ')
