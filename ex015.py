print('CALCULADORA DE LOCADORA DE VEÍCULOS')
km = float(input('Informe a quantidade de km percorridos: '))
dias = float(input('Informe a quantidade de dias de locação: '))
diaria = float(input('Informe o valor da diária: R$ '))
kmrodado = float(input('Informe o valor do km rodado: '))
print('''O veículo percorreu {}km.
Ficou locado por {} dias.
Total a ser pago R$ {:.2f}.'''.format(km, dias, (km * kmrodado) + (dias * diaria)))
