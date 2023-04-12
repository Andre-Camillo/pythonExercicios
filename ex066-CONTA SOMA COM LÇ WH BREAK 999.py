print('CONTA SOMA COM LÇ WH BREAK 999')
cont = soma = 0
while True:
    num = int(input('Informe um valor: '))
    if num == 999:
        break
    else:
       soma += num
       cont += 1
print(f'''Ao todo foram digitados {cont} números. 
A soma dos valores equivale a: {soma}.''')

