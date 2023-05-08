num = ('DIGITE O 1º VALOR: ', 'DIGITE O 2º VALOR: ', 'DIGITE O 3º VALOR: ', 'DIGITE O 4º VALOR: ')
n1 = str(input(num[0]))
n2 = str(input(num[1]))
n3 = str(input(num[2]))
n4 = str(input(num[3]))
num = n1, n2, n3, n4
print(num)
print(f'{num.count(9)}')
