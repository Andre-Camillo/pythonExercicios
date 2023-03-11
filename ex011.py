print('MEDE ÁREA² E QUANTIDADE DE TINTA')
larg = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
print('''Largura: {}m x Altura: {}m'
Área: {}
Qaunt. de tinta: {} litro(s)'''.format(larg, alt, (larg * alt), (larg * alt) / 2))
