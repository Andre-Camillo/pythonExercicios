print('O MAIS E O MENOS PESADO DENTRE 5')
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('INFORME O PESO DA {}ª PESSOA: '.format(c)))
    if peso == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso foi de {} Kg.'.format(maior))
print('O MENOR peso foi de {} Kg.'.format(menor))
