galera = list()
dados = list()
contPess = maisP = menosP = 0
nomeMaisP = nomeMenosP = ''

while True:
    dados.append(str(input('INFORME O SEU NOME: ')))
    dados.append(float(input('INFORME O SEU PESO: ')))
    galera.append(dados[:])
    dados.clear()
    contPess += 1
    contin = str(input('DESEJA CONTINUAR? [S] ou [N]: '))

    for p in galera:
        if p == 1:
            maisP = menosP = p[1]
            nomeMenosP = nomeMaisP = p[0]
        else:
            if p[1] > maisP:
                maisP = p[1]
                nomeMaisP = p[0]
            if p[1] < menosP:
                menosP = p[1]
                nomeMenosP = p[0]

    while contin not in 'SsNn':
        contin = str(input('VOCÊ DEVE DIGITAR [S] ou [N]: '))

    if contin in 'Nn':
        break

print(f'{contPess} PESSOA(S) CADASTRADA(S).\nO MAIS PESADO: {nomeMaisP} COM {maisP}Kg.\nO MAIS LEVE: {nomeMenosP} COM {menosP}Kg.')
