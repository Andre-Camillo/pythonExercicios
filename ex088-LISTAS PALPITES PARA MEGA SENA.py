from random import randint
from time import sleep
lista = []
jogos = list()
quant = int(input('INFORME A QUANTIDADE DO JOGOS: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 80)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 5:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    if i < 9:
        print(f'JOGOS 0000{i + 1}: {l}')
    elif i < 99:
        print(f'JOGOS 000{i + 1}: {l}')
    elif i < 999:
        print(f'JOGOS 00{i + 1}: {l}')
    elif i < 9999:
        print(f'JOGOS 0{i + 1}: {l}')


    #sleep(0.8)
