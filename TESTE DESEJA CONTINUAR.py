while True:
    val = int(input('DIGITE UM VALOR: '))
    contin = str(input('DESEJA CONTINUAR? [S] ou [N]: '))
    if contin in 'Nn':
        break
    while contin not in 'SsNn':
        contin = str(input('VOCÊ DEVE DIGITAR [S] ou [N]: '))







