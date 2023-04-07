print('SORTEADOR DE ALUNOS 2')
from random import choice
for alunos in range(1, 5):
    str(input('Informe o nome do {}° aluno: '.format(alunos)))
lista = [1, 2, 3, 4]
esc = choice(lista)
print('O(a) escolhido(a) foi: {}.'.format(esc))
