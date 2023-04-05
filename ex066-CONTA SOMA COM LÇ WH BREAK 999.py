print('CONTA SOMA COM LÇ WH BREAK 999')
soma = cont = num = 0
while num != 999:
    num = int(input('DIGITE UM VALOR: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'''Ao todo foram digitados {cont} números. 
A soma dos valores equivale a: {soma}.''')

