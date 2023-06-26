contin = ''
#media = 0
nome = []
n1 = []
n2 = []
while True:
    nome.append(str(input('INFORME O NOME DO ALUNO: ')))
    n1.append(float(input('1ª NOTA: ')))
    n2.append(float(input('2ª NOTA: ')))
    nome.append(n1[:])
    n1.clear()
    nome.append(n2[:])
    n2.clear()
    contin = str(input('DESEJA CONTINUAR? [S] ou [N]: '))
    if contin in 'Nn':
        print('-=' * 20)
        print(f'NOME            MEDIA ')
        for c in nome:
            print(f'{c}')


