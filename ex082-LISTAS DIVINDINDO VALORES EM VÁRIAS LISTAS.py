lista1 = []
lista2 = lista3 = 0
seguir = ''
while True:
    lista1.append(int(input('DIGITE UM VALOR: ')))
    seguir = str(input('DESEJA CONTINUAR [S] ou [N]: '))
    if seguir in 'Nn':
        break
    while seguir not in 'SsNn':
        seguir = str(input('VOCÊ DEVE DIGITAR [S] ou [N]: '))

for c in lista1:
    if c % 2 == 0:
        lista2 = lista1
    else:
        lista3 = lista1

    print(f'LISTA 01: {c}', end=' ')
    #print(f'LISTA 02: {c}')
    #print(f'LISTA 03: {c}')
