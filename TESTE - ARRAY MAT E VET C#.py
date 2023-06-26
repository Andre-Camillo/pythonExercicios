lista = list()
print('DIGITE 15 NÚMEROS INTEIROS...')
for n in range(0, 6):
    lista.append(int(input(f'{n + 1}º NÚMERO: ')))
lista = list(range(0, 15, 2))
print(lista)

