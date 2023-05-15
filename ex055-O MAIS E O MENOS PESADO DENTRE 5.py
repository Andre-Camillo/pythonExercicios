print('O MAIS E O MENOS PESADO DENTRE 5')
maior = menor = 0
for p in range(1, 4):
    peso = float(input(f'INFORME O PESO DA {p}ª PESSOA: '))
    if p == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MAIOR peso foi de {maior} Kg.')
print(f'O MENOR peso foi de {menor} Kg.')
