from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('OS NÚMEROS SORTEADOS FORAM:')
for pos, c in enumerate(num):
    print(f'{pos + 1}º NÚMERO: {c}')
print(f'\nO MAIOR VALOR: {max(num)}\nO MENOR VALOR: {min(num)}')
