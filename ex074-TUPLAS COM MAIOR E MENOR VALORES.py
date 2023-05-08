from random import randint
maior = menor = 0
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('NÚMEROS SORTEADOS:')
for pos, c in enumerate(num):
    print(f'{pos + 1}º NÚMERO: {c}')
print(f'\nO MAIOR: {max(num)}.\nO MENOR: {min(num)}.\n')

numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
print(f'NÚMEROS SORTEADOS: {numeros}.\nO MAIOR VALOR: {max(numeros)}.\nO MENOR VALOR: {min(numeros)}.')

