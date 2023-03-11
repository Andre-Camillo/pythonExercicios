print('TABUADA')
num = int(input('Digite um número inteiro para saber sua Tabuada até o 10: '))
print('TABUADA DO {}'.format(num))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))

#print('''{} x 1 = {}
#{} x 2 = {}
#{} x 3 = {}
#{} x 4 = {}
#{} x 5 = {}
#{} x 6 = {}
#{} x 7 = {}
#{} x 8 = {}
#{} x 9 = {}
#{} x 10 = {}'''.format(num, num * 1, num, num * 2, num, num * 3, num, num * 4, num, num * 5
#                       , num, num * 6, num, num * 7, num, num * 8, num, num * 9, num, num * 10))

