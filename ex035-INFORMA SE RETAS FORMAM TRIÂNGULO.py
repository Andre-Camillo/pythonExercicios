print('INFORMA SE RETAS FORMAM TRIÂNGULO')
r1 = float(input('Informe o tamanho da primeira reta: '))
r2 = float(input('informe o tamanho da segunda reta: '))
r3 = float(input('Informe o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('''As retas: {} - {} - {} \033[1;32mFORMAM\033[m um triângulo.'''.format(r1, r2, r3))
else:
    print('''As retas: {} - {} - {} \033[1;31mNÃO FORMAM\033[m um triângulo.'''.format(r1, r2, r3))