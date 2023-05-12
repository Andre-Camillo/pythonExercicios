
val = list()
val.append(1)
val.append(2)
val.append(3)
for pos, c in enumerate(val):
    print(f'NA POSIÇÃO {pos + 1} ESTÁ O VALOR: {c}')

for c in range(0, 3):
    val.append(int(input('INSIRA O VALOR: ')))

for pos, l in enumerate(val):
    print(f'NA POSIÇÃO {pos + 1} ESTÁ O VALOR: {l}')
    print(f'{l}', end=' ')
print('')
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'LISTA A: {a}')
print(f'LISTA B: {b}')
lanche = ['hamberger', 'suco', 'pizza', 'pudim']
print('')
for c in lanche:
    print(f"{c}", end=' ')
lanche[3] = "torta"
print(f'\n\n{lanche}')
lanche[0] = 'carro'
print(f'\n{lanche}')
lanche.append('cookie')
print(f'\n{lanche}')
lanche[4] = 'bolacha'
print(f'\n{lanche}')
lanche.insert(0, 'refri')
print(f'\n{lanche}')

palavras = ('aprender', 'programar', 'liguagem', 'python', 'praticar', 'trabalhar', 'mercado', 'programador')
for c in palavras:
    print(f'\nNA PALAVRA \033[1;36m{c.upper()}\033[m TEMOS: ',end='')
    for l in c:
        if l in 'aeiou':
            print(f'{l}', end='')
