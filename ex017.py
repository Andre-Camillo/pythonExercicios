from math import hypot
print('CALCULADORA DE HIPOTENUSA')
catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
print('''O cateto oposto mede: {}.
O cateto adjacente mede: {}.
A hipotenusa mede: {:.2f}. '''.format(catop, catadj, (hypot(catop, catadj))))

print('''O cateto oposto mede: {}.
O cateto adjacente mede: {}.
A hipotenusa mede: {:.2f}. '''.format(catop, catadj, (catop ** 2 + catadj ** 2) ** (1/2)))
