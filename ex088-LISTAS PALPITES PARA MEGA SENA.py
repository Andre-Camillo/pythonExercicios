from random import randint
qt_Jgs = int(input('INFORME A QUANTIDADE DE JOGOS: '))
for q in range(1, qt_Jgs + 1):
    print(f'\nJOGO Nº {q}', end=' ')
    for c in range(1, 7):
        nums = randint(1, 60)
        print(f'[{nums}]', end=' ')

