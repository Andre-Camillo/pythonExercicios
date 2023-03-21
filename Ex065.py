quant = num = soma = maior = menor = 0
resp = 's'
while resp in 'Ss':
    num = int(input('INFORME UM VALOR: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar [S] ou [N]: ')).strip()
print('Ao todo foram digitados: {} valores.\nTotalizando: {}.\nA media aritmética foi de: {}.\nO maior: {}.\nO menor: {}. Fim...'
      ''.format(quant, soma, soma / quant, maior, menor))
