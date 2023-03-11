print('ANALISANDO TRIÂNGULOS')
l1 = float(input('Informe o tamanho da 1ª linha: '))
l2 = float(input('Informe o tamanho da 2ª linha: '))
l3 = float(input('Informe o tamanho da 3ª linha: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('As linhas {} - {} - {} \033[1;32mFORMAM\033[m um triângulo.'.format(l1, l2, l3))
    if l1 == l2 == l3:
        print('Do tipo "EQUILÁTERO"')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Do tipo "ESCALENO"')
    elif l1 != l2 or l1 != l3 or l2 != l3:
        print('Do tipo "ISOSCELES"')
else:
    print('As linhas {} - {} - {} \033[1;31mNÃO FORMAM\033[m um triângulo.'.format(l1, l2, l3))
    