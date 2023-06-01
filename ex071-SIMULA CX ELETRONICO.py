from num2words import num2words
print('SIMULADOR DE CAIXA ELETRÔNICO')
valor = int(input('INFORME O VALOR DO SAQUE: R$ '))
num = valor
ced = 100
totalced = 0
while True:
    if valor >= ced:
        valor -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'{totalced} CÉDULAS DE R$ {ced:.2f}')
        #elif ced == 10000:
        #    ced = 5000
        #elif ced == 5000:
        #    ced = 1000
        #elif ced == 1000:
        #    ced = 500
        #elif ced == 500:
        #    ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1

        totalced = 0
        if valor == 0:
            break
print(f"\nEM CARDINAL: {num2words(num, lang='pt-br').upper()} REAIS.\nEM ORDINAL: {num2words(num, lang='pt-br', to='ordinal').upper()}.")


