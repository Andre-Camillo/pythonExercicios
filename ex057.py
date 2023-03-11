#MÉTODO ENXUTO
#sex = str(input('INFORME SEU SEXO: ')).strip()[0]
#while sex not in 'MmFf':
#    sex = str(input('Você digitou "{}".\nFavor digitar "M" ou "F": '.format(sex).upper()))
#print('Sexo "{}". Registrado com sucesso.'.format(sex).upper())

#MÉTODO COMPLETO
from emoji import emojize
color = {'clear': '\033[m', 'red': '\033[1;31m', 'green': '\033[1;32m',
         'cyan': '\033[1;36m', 'purple': '\033[1;35m', 'yellow': '\033[1;33m'}
sex = str(input('INFORME O SEU SEXO [M] ou [F]: ')).strip().lower()
while sex[0] not in 'mf'.strip():
    sex = str(input('VOCÊ DIGITOU: {}"{}"{}.\nVOCÊ DEVE DIGITAR: {}"[M]" ou "[F]"{}: '
                    .format(color['red'], sex.upper().strip(), color['clear'], color['yellow'], color['clear'])).lower())
if 'm' in sex[0]:
    print('SEXO REGISTRADO COM SUCESSO -{} "MASCULINO"{}.'.format(color['cyan'], color['clear']))
elif 'f' in sex[0]:
    print('SEXO REGISTRAD COM SUCESSO -{} "FEMININO"{}.'.format(color['purple'], color['clear']))
print('GRATO POR UTILIZAR NOSSOS SERVIÇOS {}'.format(emojize(":thumbs_up:")))
