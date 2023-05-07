lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinza', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('ESCOLHA UM NÚMERO ENTRE "0" E "20": '))
while True:
    if num < 0 or num > 20:
        num = int(input('VOCÊ DEVE ESCOLHER UM NÚMERO ENTRE "0" E "20": '))
    else:
        for c in lista:
            print(lista[num])
            break
        cont = str(input('DESEJA CONTINUAR? [S] ou [N]: ')).upper()
        if cont not in 'SsNn':
            num = int(input('VOCÊ DEVE ESCOLHER [S] ou [N]: '))
        elif cont == 'S':
            num = int(input('ESCOLHA UM NÚMERO ENTRE "0" E "20": '))
        else:
            break
