val = list()
for c in range(0, 5):
    num = int(input(f'INSIRA O {c + 1}º VALOR: '))
    if c == 0:
        val.append(num)
        print('ADICIONADO AO FINAL DA LISTA')
    elif num > val[-1]:
        val.append(num)
    else:
        pos = 0
        while pos < len(val):
            if num <= val[pos]:
                val.insert(pos, num)
                print(f'ADICIONADO NA POSIÇÃO: {pos + 1}')
                break
            pos += 1
print(f'OS NÚMEROS DIGITADOS "ORDENADAMENTE" FORAM: ', end='')
for l in val:
    print(f'{l}', end=' ')

