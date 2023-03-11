print('REAJUSTADOR SALARIAL')
salario = float(input('Informe o salario a ser reajustado: R$ '))
if salario > 1250:
    print('''Salário atual: R$ {:.2f}.
Salário reajustado: R$ {:.2f}.'''.format(salario, salario + salario * 10 / 100))
else:
    print('''Salário atual: R$ {:.2f}.
Salário reajustado: R$ {:.2f}.'''.format(salario, salario + salario * 15 / 100))

#> 1250 + 10%
#<= 1250 + 15%
