print('SORTEADOR DE ALUNOS')
import random
n1 = str(input('Informe o nome do 1º aluno: '))
n2 = str(input('Informe o nome do 2º aluno: '))
n3 = str(input('Informe o nome do 3º aluno: '))
n4 = str(input('Informe o nome do 4º aluno: '))
lista = [n1, n2, n3, n4]
print('O aluno(a) sortedo(a) para apagar o quadro é: {}'.format(random.choice(lista)))
