print('SIMULADOR DE CAIXA ELETRÔNICO')
valor = int(input('INFORME O VALOR DO SAQUE: R$ '))
ced = 1000
totalCed = 0
while True:
    if valor >= ced:
        valor -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'{totalCed} CÉDULAS DE R$ {ced:.2f}')
        if ced == 1000:
            ced = 500
        elif ced == 500:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if valor == 0:
            break



