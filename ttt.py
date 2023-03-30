#import math
from math import pow, sqrt, hypot

n1 = int(input('DIGITE UM NÚMERO: '))
n2 = int(input('DIGITE UM NÚMERO: '))

print(f'A raiz de {n1} é: {sqrt(n1)}')

print(f'{n1} ao quadrado é: {pow(n1, 2)}')

print(f'A hipotenusa dos catetos A e B é: {hypot(n1, n2)}.')
