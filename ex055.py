print('O MAIS E O MENOS PESADO DENTRE 5')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if maior > peso:
            maior = peso
        if menor < peso:
            menor = peso
print('O MAIS PESADO: {}'.format(maior))
print('O MAIS LEVE: {}'.format(menor))
