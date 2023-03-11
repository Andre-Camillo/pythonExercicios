print('MEDIA ESCOLAR')
n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))
n3 = float(input('Informe a terceira nota do aluno: '))
n4 = float(input('Informe a quarta nota do aluno: '))
media = (n1 + n2 + n3 + n4) / 4
print('''1º Trimestre - Nota {:.2f}
2º Trimestre - Nota {:.2f}
3º Trimestre - Nota {:.2f}
4º Trimestre - Nota {:.2f}
\033[1;36mSua Media foi: {:.2f}\033[m'''.format(n1, n2, n3, n4, media))
if media < 5:
    print('\033[1;31m"REPROVADO(A)"\033[m')
elif media <= 6.9:
    print('\033[1;33m"VOCÊ ESTÁ EM RECUPERAÇÃO"\033[m')
else:
#elif media >= 7:
    print('\033[1;32m"VOCÊ FOI APROVADO(A)"\033[m')
