print('CONVERSOR DE BASES NUMÉRICAS')
num = int(input('Digite um número inteiro: '))
base = int(input('''[ 1 ] PARA BINÁRIO
[ 2 ] PARA OCTAL
[ 3 ] PARA HEXADECIMAL
INFORME A BASE DE CONVERSÃO: '''))
if base == 1:
    print('{} DECIMAL CONVERTIDO PARA BINÁRIO EQUIVALE A: {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} DECIMAL CONVERTIDO PARA OCTAL EQUIVALE A: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} DECIMAL CONVERTIDO PARA HEXADECIMAL EQUIVALE A: {}'.format(num, hex(num)[2:]))
