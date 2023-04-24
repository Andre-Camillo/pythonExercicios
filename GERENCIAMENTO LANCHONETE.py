from emoji import emojize
from time import sleep
#CÓD EMOJIS UTILIZADOS
#bauru :sandwich: - lanche :hamburger: - copo refri :cup_with_straw: - dinheiro :heavy_dollar_sign:
colors = {'clear': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'purple': '\033[35m', 'cyan': '\033[36m'}
quantxTudo = quantxEgg = quantxSalada = quantBauru = quantCoca = quantGuarana = quantFanta = quantTubaina = 0
contxTudo = contxEgg = contxSalada = contBauru = contCoca = contGuarana = contFanta = contTubaina = 0
ttxTudo = ttxEgg = ttxSalada = ttBauru = ttCoca = ttGuarana = ttFanta = ttTubaina = 0
opc = 9999

# CADASTRE AQUI O VALOR DOS PRODUTOS:
vlxTudo = 10
vlxEgg = 9
vlxSalada = 7
vlBauru = 5
vlCoca = 8
vlGuarana = 7
vlFanta = 6
vlTubaina = 5

print(f"""{'=' * 44}
{'=' * 14} ANDRE'S LANCHES {'=' * 13}
{'=' * 44}""")

while opc != 0:
    opc = int(input(f"""
{'*' * 44}
{'*' * 12}   MENU PRINCIPAL   {'*' * 12}
{'*' * 44}
{'*' * 12}   1) - LANCHES   {'*' * 14}
{'*' * 12}   2) - BEBIDAS   {'*' * 14}
{'*' * 12}   3) - CONTA   {'*' * 16}
{'*' * 12}   0) - SAIR   {'*' * 17}
{'*' * 44}

ESCOLHA SUA OPÇÃO: """))

    if opc == 1:
        menuLanche = int(input(f'''{emojize(':hamburger:')*18}
{emojize(':hamburger:')*5}   MENU LANCHES  {emojize(':hamburger:')*6}
{emojize(':hamburger:')*18}
{emojize(f':hamburger:')*5}   {colors['green']}1) - X-TUDO{colors['clear']}   {emojize(':hamburger:')*6}
{emojize(f':hamburger:')*5}   {colors['yellow']}2) - X-EGG{colors['clear']}    {emojize(':hamburger:')*6}
{emojize(f':hamburger:')*5}   {colors['cyan']}3) - X-SALADA{colors['clear']} {emojize(':hamburger:')*6}
{emojize(f':hamburger:')*5}   {colors['purple']}4) - BAURÚ{colors['clear']}    {emojize(':hamburger:')*6}
{emojize(f':hamburger:')*5}   {colors['red']}0) - VOLTAR{colors['clear']}   {emojize(':hamburger:')*6}
{emojize(f':hamburger:')*18}

ESCOLHA SEU LANCHE: '''))
        if menuLanche == 1:
            print(f"ESCOLHEU {colors['green']}X-TUDO{colors['clear']} {emojize(':hamburger:')}")
            print('')
            quantxTudo = int(input('ESCOLHA A QUANTIDADE: '))
            contxTudo += quantxTudo
        if menuLanche == 2:
            print(f"ESCOLHEU X-EGG {emojize(':hamburger:')}")
            print('')
            quantxEgg = int(input('ESCOLHA A QUANTIDADE: '))
            contxEgg += quantxEgg
        if menuLanche == 3:
            print(f"ESCOLHEU X-SALADA {emojize(':hamburger:')}")
            print('')
            quantxSalada = int(input('ESCOLHA A QUANTIDADE: '))
            contxSalada += quantxSalada
        if menuLanche == 4:
            print(f"ESCOLHEU BAURÚ {emojize(':sandwich:')}")
            print('')
            quantBauru = int(input('ESCOLHA A QUANTIDADE: '))
            contBauru += quantBauru

    if opc == 2:
        menuBebidas = int(input(f'''{emojize(':cup_with_straw:')*21}
{emojize(':cup_with_straw:')*6}   MENU BEBIDAS  {emojize(':cup_with_straw:')*7}
{emojize(':cup_with_straw:')*21}
{emojize(f':cup_with_straw:')*6}   {colors['green']}1) - COCA-COLA{colors['clear']}  {emojize(':cup_with_straw:')*6}
{emojize(f':cup_with_straw:')*6}   {colors['cyan']}2) - GUARANÁ{colors['clear']}    {emojize(':cup_with_straw:')*6}
{emojize(f':cup_with_straw:')*6}   {colors['yellow']}3) - FANTA{colors['clear']}      {emojize(':cup_with_straw:')*6}
{emojize(f':cup_with_straw:')*6}   {colors['purple']}4) - TUBAÍNA{colors['clear']}    {emojize(':cup_with_straw:')*6}
{emojize(':cup_with_straw:')*6}   {colors['red']}0) - VOLTAR{colors['clear']}     {emojize(':cup_with_straw:')*6}
{emojize(':cup_with_straw:')*21}

ESCOLHA SUA BEBIDA: '''))
        if menuBebidas == 1:
            print(f"ESCOLHEU {colors['green']}COCA-COLA{colors['clear']} {emojize(':cup_with_straw:')}")
            print('')
            quantCoca = int(input('ESCOLHA A QUANTIDADE: '))
            contCoca += quantCoca
        if menuBebidas == 2:
            print(f"ESCOLHEU {colors['cyan']}GUARANÁ{colors['clear']} {emojize(':cup_with_straw:')}")
            print('')
            quantGuarana = int(input('ESCOLHA A QUANTIDADE: '))
            contGuarana += quantGuarana
        if menuBebidas == 3:
            print(f"ESCOLHEU {colors['yellow']}FANTA{colors['clear']} {emojize(':cup_with_straw:')}")
            print('')
            quantFanta = int(input('ESCOLHA A QUANTIDADE: '))
            contFanta += quantFanta
        if menuBebidas == 4:
            print(f"ESCOLHEU {colors['purple']}TUBAÍNA{colors['clear']} {emojize(':cup_with_straw:')}")
            print('')
            quantTubaina = int(input('ESCOLHA A QUANTIDADE: '))
            contTubaina += quantTubaina

    if quantxTudo or quantxEgg or quantxSalada or quantBauru or quantCoca or quantGuarana or quantFanta or quantTubaina > 0:
        print('')
        print('=' * 44)
        parcial = print(f"{' ' * 19}PEDIDO")
        print('-' * 44)
        if quantxTudo > 0:
            print(f"{contxTudo} - {colors['green']}X-TUDO{colors['clear']}      UNI R$ {vlxTudo:.2f} - TOT R$ {contxTudo * vlxTudo:.2f}")
            ttxTudo = contxTudo * vlxTudo
        if quantxEgg > 0:
            print(f"{contxEgg} - {colors['yellow']}X-EGG{colors['clear']}       UNI R$  {vlxEgg:.2f} - TOT R$ {contxEgg * vlxEgg:.2f}")
            ttxEgg = contxEgg * vlxEgg
        if quantxSalada > 0:
            print(f"{contxSalada} - {colors['cyan']}X-SALADA{colors['clear']}    UNI R$  {vlxSalada:.2f} - TOT R$ {contxSalada * vlxSalada:.2f}")
            ttxSalada = contxSalada * vlxSalada
        if quantBauru > 0:
            print(f"{contBauru} - {colors['purple']}BAURÚ{colors['clear']}       UNI R$  {vlBauru:.2f} - TOT R$ {contBauru * vlBauru:.2f}")
            ttBauru = contBauru * vlBauru
        if quantCoca > 0:
            print(f"{contCoca} - {colors['green']}COCA-COLA{colors['clear']}   UNI R$  {vlCoca:.2f} - TOT R$ {contCoca * vlCoca:.2f}")
            ttCoca = contCoca * vlCoca
        if quantGuarana > 0:
            print(f"{contGuarana} - {colors['cyan']}GUARANÁ{colors['clear']}     UNI R$  {vlGuarana:.2f} - TOT R$ {contGuarana * vlGuarana:.2f}")
            ttGuarana = contGuarana * vlGuarana
        if quantFanta > 0:
            print(f"{contFanta} - {colors['yellow']}FANTA{colors['clear']}       UNI R$  {vlFanta:.2f} - TOT R$ {contFanta * vlFanta:.2f}")
            ttFanta = contFanta * vlFanta
        if quantTubaina > 0:
            print(f"{contTubaina} - {colors['purple']}TUBAÍNA{colors['clear']}     UNI R$  {vlTubaina:.2f} - TOT R$ {contTubaina * vlTubaina:.2f}")
            ttTubaina = contTubaina * vlTubaina
    if opc == 3:
        print('=' * 44)
        print(f'''VALOR A PAGAR: {' ' * 20}R$ {ttxTudo + ttxEgg + ttxSalada + ttBauru + ttCoca + ttGuarana + ttFanta + ttTubaina:.2f}''')
        print('=' * 44)
        print('')
        fin = str(input('''SEU PEDIDO ESTÁ COMPLETO?
    S - PARA SIM
    N - PARA NÃO: '''))
        if fin[0] in 'sS':
            print('')
            pgto = str(input('''ESCOLHA A FORMA DE PAGAMENTO:
    1) DINHEIRO
    2) CARTÃO
    3) VOUCHER '''))
            print(f"{colors['green']}PROCESSANDO{colors['clear']}", end='')
            sleep(.5)
            print('.', end='')
            sleep(.5)
            print('.', end='')
            sleep(.5)
            print('.', end='')
            sleep(.5)
            print('.', end='')
            sleep(.5)
            print('.')
            sleep(.5)
            print('')
            print('IMPRIMINDO', end='')
            sleep(.5)
            print('.', end='')
            sleep(.5)
            print('.', end='')
            sleep(.5)
            print('.', end='')
            sleep(.5)
            break
        elif fin[0] in 'nN':
            opc = opc
