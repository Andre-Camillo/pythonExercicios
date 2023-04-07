print('SOMA DOS PARES')
soma = 0
for c in range(1, 7):
    num = int(input('informe o {}° número: '.format(c)))
    if num % 2 == 0:
        soma += num
print('Total da soma dos número pares: {}'.format(soma))
