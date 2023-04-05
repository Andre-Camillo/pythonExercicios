print('SOMA ÍMPARES MÚLTIPLOS DE 3')
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print('Total: {}'.format(soma, end=' '))
