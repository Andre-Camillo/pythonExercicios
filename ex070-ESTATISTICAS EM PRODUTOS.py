
maisBarato = mais1000 = contValor = nomeProd = valorProd = 0
contin = str(input('Poderia colaborar com nossa pesquisa? [S] ou [N]: ')).strip()
while contin[0] not in 'Nn':
    if contin[0] not in 'SsNn':
        contin = str(input('Poderia colaborar com nossa pesquisa? [S] ou [N]: ')).strip()
    else:
        nomeProd = str(input('Informe o nome do produto: '))
        valorProd = float(input('Informe o valor do produto: R$ '))
        contValor += valorProd
        contin = str(input('Deseja continuar? '))
        while contin[0] not in 'SsNn':
            contin = str(input('Digite [S] ou [N]: ')).strip()
        if valorProd > 1000:
            mais1000 += 1

        if maisBarato == 1:
            maisBarato = valorProd
        else:
            if valorProd > maisBarato:
                maisBarato = valorProd
            if valorProd < maisBarato:
                maisBarato = valorProd

print(f'Total de gastos: {contValor:.2f}')
print(f'Quantidaade de produtos acima de R$ 1.000,00: {mais1000}')
print(f'O produto mais barato custa: {maisBarato:.2f}')
