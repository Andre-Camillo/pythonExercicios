listagem = ('Lápis ', 1.75, 'Borracha ', 2, 'Caderno ', 15.90, 'Estojo ', 25, 'Transferidor ', 4.20,
            'Compasso ', 9.99, 'Mochila ', 120.32, 'Canetas ', 22.30, 'Livro ', 34.90)
print('-' * 30)
print(' ' * 5, 'LISTAGEM DE PREÇOS')
print('-' * 30)
for c in range(len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<20}', end='')
    else:
        print(f' R$ {listagem[c]:>6.2f}')
print('-' * 30)
