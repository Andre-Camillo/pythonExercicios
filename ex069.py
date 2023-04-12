print('=' * 22)
print('     PAR ou IMPAR')
print('=' * 22)
from random import randint
cont = par = impar = 0
comput = randint(1, 5)
while True:
    cont += 1
    user = int(input('       OPÇÕES: \nPARA IMPAR DIGITE [1]\n PARA PAR DIGITE [2]\n ESCOLHA SUA OPÇÃO: '))

    soma = comput + user

    if user == 1:
        print(f'Você escolheu IMPAR\nPC escolheu PAR')
    else:
        print(f'Você escolheu PAR\nPC escpolheu IMPAR')

    if soma % 2 == 0 and user == 2:
        print(f'{soma} é PAR"\nParabéns!!! Você venceu!!!')
    elif soma % 2 == 1 and user == 1:
        print(f'{soma} é IMPAR"\nParabéns!!! Você venceu!!!')



