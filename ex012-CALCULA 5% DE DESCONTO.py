print('CALCULA 5% DE DESCONTO')
valor = float(input('Informe o valor do produto: R$ '))
desc = float(input('Informe o percentual de desconto: '))
print('''Valor atual: R$ {:.2f}.
Valor com Desconto: R$ {:.2f}. '''.format(valor, valor - valor * desc / 100))

