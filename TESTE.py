val = list()
mai = men = 0
for c in range(0, 5):
    val.append(int(input(f'DIGITE O {c + 1}º VALOR: ')))
    if c == 0:
        mai = men = val[c]
    else:
        if val[c] > mai:
            mai = val[c]
        if val[c] < men:
            men = val[c]

print(f'O MAIOR VALOR: {mai}')
print(f'O MENOR VALOR: {men}')

print(f'O MAIOR ESTÁ NA POSIÇÃO: ', end=' ')
for i, v in enumerate(val):
    if v == mai:
        print(i + 1)

print(f'O MENOR ESTÁ NA POSIÇÃO: ', end=' ')
for i, v in enumerate(val):
    if v == men:
        print(i + 1)


