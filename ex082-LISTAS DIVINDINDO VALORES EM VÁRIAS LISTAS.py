from time import sleep
lista1 = lista2 = lista3 = list()
seguir = ''
while True:
    lista1.append(int(input('DIGITE UM VALOR: ')))
    seguir = str(input('DESEJA CONTINUAR [S] ou [N]: '))
    if seguir[0] in 'Nn':
        break
    while seguir[0] not in 'SsNn':
        seguir = str(input('VOCÊ DEVE DIGITAR [S] ou [N]: '))
print('\033[1mProcessando\033[m',end='')
sleep(0.5)
print('\033[1m.\033[m', end='')
sleep(0.5)
print('\033[1m.\033[m', end='')
sleep(0.5)
print('\033[1m.\033[m', end='')
sleep(0.5)
print(f'\nVALORES DIGITADOS: ', end='')
for b in lista1:
    print(f'{b}', end=' ')
print(f'\nNÚMEROS PARES: ', end='')
for c in (lista1):
    if c % 2 == 0:
        lista2 = lista1
        print(f'{c}', end=' ')
print(f'\nNÚMEROS ÍMPARES: ', end='')
for d in (lista1):
    if d % 2 == 1:
        lista3 = lista1
        print(f'{d}', end=' ')

