from datetime import date
op = - 1
ano_atual = date.today().year
while op != 0:
    op = int(input(
        '========== OPÇÕES ==========\nDIGITE [ 1 ] PARA PROSSEGUIR\nDIGITE [ 0 ] PARA SAIR\nESCOLHA SUA OPÇÃO: '))
    ano_nasc = int(input('INFORME O ANO DE SEU NASCIMENTO [XXXX]: '))
    idade = ano_atual - ano_nasc
    sexo = str(input('INFORME O SEU SEXO [M] ou [F]: '))
    if sexo in 'Mm':
        print(f'Tens {idade} ano(s) e é do sexo Masculino.')
    elif sexo in 'Ff':
        print(f'Tens {idade} ano(s) e é do sexo Feminino.')
    else:
        while sexo != sexo in 'Mm' or 'Ff':
            print('Você deve digitar "M" ou "F"')
            sexo = str(input('INFORME O SEU SEXO [M] ou [F]: '))

print('OPÇÃO REGISTRADA COM SUCESSO')

