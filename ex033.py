print('MOSTRA O MAIOR E O MENOR ENTRE "3"')
v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
v3 = int(input('Digite o 3° valor: '))
if v1 < v2 and v3:
    menor = v1
if v2 < v1 and v3:
    menor = v2
if v3 < v1 and v2:
    menor = v3
if v1 > v2 and v3:
    maior = v1
if v2 > v1 and v3:
    maior = v2
if v3 > v1 and v2:
    maior = v3
print('O MAIOR VALOR É O: {}'.format(maior))
print('O MENOR VALOR É O: {}'.format(menor))
