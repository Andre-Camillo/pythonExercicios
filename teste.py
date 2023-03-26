soma = cont = num = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor: '))

print(f'Ao todo foram digitados {cont}, totalizando {soma}.')
