from datetime import date
op = str(input('========== OPÇÕES ==========\nDIGITE [ 1 ] PARA PROSSEGUIR\nDIGITE [ 0 ] PARA SAIR\nESCOLHA SUA OPÇÃO: '))
while op != 0:
    ano_nasc = int(input('INFORME O ANO DE SEU NASCIMENTO [XXXX]: '))
    sexo = str(input('INFORME O SEU SEXO [M] ou [F]: '))

    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if sexo in 'Mm':
        print(f'Tens {idade} ano(s) e é do sexo Masculino.')
    elif sexo in 'Ff':
        print(f'Tens {idade} ano(s) e é do sexo Feminino.')
    else:
        print('Você deve digitar o ano de seu nascimento: [XXXX]')
        ano_nasc = int(input('INFORME O ANO DE SEU NASCIMENTO: '))
        sexo = str(input('INFORME O SEU SEXO [M] ou [F]: '))
    op = str(input(
        '========== OPÇÕES ==========\nDIGITE [ 1 ] PARA PROSSEGUIR\nDIGITE [ 0 ] PARA SAIR\nESCOLHA SUA OPÇÃO: '))
print('OPÇÃO REGISTRADA COM SUCESSO')

    #break