v1 = int(input('INFORME O 1° VALOR: '))
v2 = int(input('INFORME O 2° VALOR: '))
num = 0
soma = 0
subt = 0
divid = 0
mult = 0
raizv1 = 0
raizv2 = 0
hipot = 0
maior = 0
circ1 = 0
circ2 = 0
while num != 10:
    num = int(input('''OPÇÕES
[ 1 ] - SOMAR
[ 2 ] - SUBTRAIR
[ 3 ] - DIVIDIR
[ 4 ] - MULTIPLICAR
[ 5 ] - RAIZ QUADRADA
[ 6 ] - HIPOTENUSA
[ 7 ] - MAIOR
[ 8 ] - CIRCUNFERÊNCIA DO RAIO
[ 9 ] - NOVOS NÚMEROS
[ 10 ] - SAIR
ESCOLHA UMA DAS OPÇÕES: '''))
    if num == 1:
        soma = v1 + v2
        print('A SOMA ENTRE {} + {} É: {}.'.format(v1, v2, soma))
    elif num == 2:
        subt = v1 - v2
        print('A SUBTRAÇÃO DE {} - {} É: {}.'.format(v1, v2, subt))
    elif num == 3:
        divid = v1 / v2
        print('A DIVISÃO DE {} / {} É: {}.'.format(v1, v2, divid))
    elif num == 4:
        mult = v1 * v2
        print('A MULTIPLICAÇÃO DE {} * {} É: {}.'.format(v1, v2, mult))
    elif num == 5:
        raizv1 = v1 ** (1/2)
        raizv2 = v2 ** (1/2)
        print('A RAIZ² DE {} É {:.2f}\nA RAIZ² DE {} É {:.2f}.'.format(v1, raizv1, v2, raizv2))
    elif num == 6:
        hipot = (v1 ** 2 + v2 ** 2) ** (1/2)
        print('A HIPOTENUSA DO CAT OP {} E DO CAT ADJ {} É: {}.'.format(v1, v2, hipot))
    elif num == 7:
        if v1 > v2:
            maior = v1
        if v1 < v2:
            maior = v2
        print('O MAIOR ENTRE {} e {} É: {}'.format(v1, v2, maior))
    elif num == 8:
        circ1 = (3.1415 * 2) * v1
        circ2 = (3.1415 * 2) * v2
        print('A CIRCUNFERÊNCIA DE {} É {:.2f}\nA CIRCUNFERÊNCIA DE {} É {:.2f}.'.format(v1, circ1, v2, circ2))
    elif num == 9:
        v1 = int(input('INFORME O 1° VALOR: '))
        v2 = int(input('INFORME O 2° VALOR: '))
    elif num < 1 or num > 10:
        print('VOCÊ DEVE ESCOLHER UM NÚMERO ENTRE "1 e 10".')
