from math import factorial
num = int(input('INFORME UM NÚMERO PARA SABER SEU FATORIAL: '))
for c in range(num, 0, -1):
    if c > 1:
        print(c, 'x ', end='')
    else:
        print(c, '= ', end='')
#    print(c, 'x' if c > 1 else '=', end=' ')
print(factorial(num))


