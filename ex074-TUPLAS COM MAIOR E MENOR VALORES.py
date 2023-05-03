from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = 0
print(f'OS VALORES SORTEADOS FORAM: ', end='')
for n in num:
    print(f"{n}", end=' ')
print(f'\nO MAIOR: {max(num)}\nO MENOR: {min(num)}')
