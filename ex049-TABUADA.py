print('TABUADA')
num = float(input('Digite um número para saber sua tabuada: '))
print('TABUADA DO {}'.format(num))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
