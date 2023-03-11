from time import sleep
prim = int(input('INFORME O 1° TERMO: '))
raz = int(input('INFORME A RAZÃO: '))
termo = prim
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += raz
    cont += 1
print('ANALIZANDO')
sleep(.5)
print('PROCESSANDO', end='')
print('.', end='')
sleep(.5)
print('.', end='')
sleep(.5)
print('.\n', end='')
sleep(.5)

acres = int(input('''DESEJA MOSTRAR MAIS TERMOS?
[1] PARA SIM
[2] PARA NÃO 
ESCOLHA UMA OPÇÃO: '''))
if acres == 1:
    mais = int(input('INFORME QUANTOS: '))


