print('SENO, COSSENO E TANGENTE')
from math import radians, sin, cos, tan
ang = float(input('''Digite um ângulo: '''))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('''O SENO do ângulo {} é: {:.2f}
O COSSENO do ângulo {} é: {:.2f}
A TANGENTE do ângulo {} é: {:.2f}'''.format(ang, seno, ang, cosseno, ang, tangente))
