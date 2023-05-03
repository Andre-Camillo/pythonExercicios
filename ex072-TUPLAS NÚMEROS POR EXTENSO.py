cont = ('zero', 'um', 'dois', 'três', 'uatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('DIGITE UM NÚMERO ENTRE 0 E VINTE: '))
    if 0 <= num <= 20:
        break
    print('NÚMERO INVÁLIDO.')
print(f'VOCÊ DIGITOU O NÚMERO: {cont[num]}')