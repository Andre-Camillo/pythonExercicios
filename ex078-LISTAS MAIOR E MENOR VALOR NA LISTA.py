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

print(f'O MAIOR NO 1º MÉTODO: {max(val)}\nO MAIOR NO 2º MÉTODO: {mai}')
print(f'O MENOR NO 1º MÉTODO: {min(val)}\nO MENOR NO 2º MÉTODO: {men}')
print(f'POSIÇÃO(ÇÕES) DO(S) MAIOR(ES) VALOR(ES): ', end='')
for i, v in enumerate(val):
    if v == mai:
        print(f'{i + 1}...', end='')
print()
print(f'POSIÇÃO(ÇÕES) DO(S) MENOR(ES) VALOR(ES): ', end='')
for i, v in enumerate(val):
    if v == men:
        print(f'{i + 1}...', end='')
