a = 2, 5, 4
b = 5, 8, 1, 2, 9, 7
c = a + b
num = 2
print(f'\nVAR A: {a} (S/ ORGANIZAR)\nVAR B: {b} (S/ ORGANIZAR)\nVAR C: {c} (S/ ORGANIZAR)')
#print(f'VAR C: {c} S/ ORGANIZAR')
print(f'VAR C: {sorted(c)} ORGANIZADA')
print(f'COM LEN: {len(c)}')
if c.count(num) >= 1:
    print(f'O NÚMERO "{num}" APARECE {c.count(num)} VEZ(ES), NA {c.index(num) + 1}ª POSIÇÃO .')
else:
    print(f'O NÚMERO "{num}" NÃO APARECE NENHUMA VEZ.')
