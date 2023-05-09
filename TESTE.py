lista = ('lapis', 1.75, 'borracha', 2, 'caderno', 15.90, 'estojo', 25, 'tranferidor', 4.20, 'compasso', 9.99,
         'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS" :^40}')
print('-' * 40)
for c in range(len(lista)):
    if c % 2 == 0:
        print(f' {lista[c]:.<27}'.upper(), end='')
    else:
        print(f' R$ {lista[c]:>7.2f}'.upper())
