print('REAJUSTA SALÁRIO')
salario = float(input('Informe o valor a se reajustado: R$ '))
reajuste = float(input('Informe o percentual de reajuste: '))
print('''Salário atual: R$ {:.2f}.
Salário reajustado: R$ {:.2f}.'''.format(salario, salario + salario * reajuste / 100))
