print('CALCUÇLADORA DE PASSAGEM RODOVIÁRIA')
km = float(input('Informe a quilometragem a ser percorrida: '))
if km <= 200:
    print('''Seu percurso será de: {} km.
Valor da passagem: R$ {:.2f}.'''.format(km, km * 0.50))
else:
    print('''Seu percurso será de: {} km.
Valor da passagem: R$ {:.2f}.'''.format(km, km * 0.45))