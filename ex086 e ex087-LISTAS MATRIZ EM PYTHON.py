m1 = []
m2 = []
m3 = []
master = []
somPar = somCol_03 = 0

for a in range(0, 3):
    m1.append(int(input(f'DIGITE UM VALOR PARA [0, {a}]: ')))

for b in range(0, 3):
    m2.append(int(input(f'DIGITE UM VALOR PARA [1, {b}]: ')))

for c in range(0, 3):
    m3.append(int(input(f'DIGITE UM VALOR PARA [2, {c}]: ')))

master.append(m1)
master.append(m2)
master.append(m3)

for t in master:
    print(f'[ {t[0]} ][ {t[1]} ][ {t[2]} ]')
    somCol_03 += t[2]
    for l in t:
        if l % 2 == 0:
            somPar += l

print(f'A SOMA DOS VALORES PARES É: {somPar}')
print(f'A SOMA DOS VALORES DA 3ª COLUNA É: {somCol_03}')
print(f'O MAIOR VALOR DA SEGUNDA LINHA: {max(master[1])}')
