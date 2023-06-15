galera = list()
dados = list()
contPess = maisP = menosP = 0
nomeMaisP = nomeMenosP = ''

while True:
    dados.append(str(input('INFORME O SEU NOME: ')))
    dados.append(float(input('INFORME O SEU PESO: ')))

    if len(galera) == 0:
        maisP = menosP = dados[1]
        nomeMenosP = nomeMaisP = dados[0]
    else:
        if dados[1] > maisP:
            maisP = dados[1]
            nomeMaisP = dados[0]
        if dados[1] < menosP:
            menosP = dados[1]
            nomeMenosP = dados[0]

    galera.append(dados[:])

    dados.clear()
    contPess += 1
    contin = str(input('DESEJA CONTINUAR? [S] ou [N]: '))

    while contin not in 'SsNn':
        contin = str(input('VOCÊ DEVE DIGITAR [S] ou [N]: '))

    if contin in 'Nn':
        break

print(f'{contPess} PESSOA(S) CADASTRADA(S).')
print(f'O MAIS PESADO: {nomeMaisP.upper()} COM {maisP}Kg.\nO MAIS LEVE: {nomeMenosP.upper()} COM {menosP}Kg.')
