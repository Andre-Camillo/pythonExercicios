print('CONVERTENDO EM DOLAR')
real = float(input('Informe o valor em reais a ser convertido em dolar: R$ '))
dolar_hoje = float(input('Informe o valor do dolar hoje: U$ '))
print('R$ {:.2f} equivalem a U$ {:.2f}'.format(real, real / dolar_hoje))
