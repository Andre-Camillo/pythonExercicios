galera = list()
dados = list()
totmai = totmen = 0
contin = ''

for c in range(0, 3):
    dados.append(str(input('NOME: ')))
    dados.append(int(input('IDADE: ')))
    galera.append(dados[:])
    dados.clear()

    for p in galera:
        if p[1] >= 21:
            print(f'{p[0]} É MAIOR DE IDADE')
            totmai += 1
        else:
            print(f'{p[0]} NÃO É MAIOR DE IDADE')
            totmen +=1




print(f'MAIORES DE 21 ANOS: {totmai}\nMENORES DE 21 ANOS: {totmen}')
