print('CONTADOR SOMADOR COM LAÇO WH')
print('+' * 22)
print('+ CONTADOR E SOMADOR +')
print('+' * 22)
num = 0
cont = - 1
soma = - 999
while num != 999:
    num = int(input('DIGITE UM NÚMERO: '))
    cont += 1
    soma += num
print('A todo foram digitados: {} números.\nA soma dos valores é: {}'.format(cont, soma))
