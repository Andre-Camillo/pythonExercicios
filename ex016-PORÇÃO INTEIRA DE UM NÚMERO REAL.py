print('PORÇÃO INTEIRA DE UM NÚMERO REAL')
from math import trunc
num = float(input('Digite um número real: '))
print('A porção inteira do número {} é {}.'.format(num, trunc(num)))
print('A porção inteira do número {} é {:.0f}.'.format(num, num))
