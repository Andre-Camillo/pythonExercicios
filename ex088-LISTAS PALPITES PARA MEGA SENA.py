from random import randint
from time import sleep
lista = []
jogos = list()
quant = int(input('INFORME A QUANTIDADE DO JOGOS: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 61)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'JOGOS {i + 1}: {l}')
    sleep(0.5)
