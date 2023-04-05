print('INDICADOR DE CATEGORIAS ETÁRIAS ESPORTIVAS')
from datetime import date
color = {'clear': '\033[m', 'red': '\033[1;31m', 'green': '\033[1;32m', 'yellow': '\033[1;33m', 'purple': '\033[1;35m', 'cyan': '\033[1;36m'}
ano_atual = date.today().year
ano_nasc = int(input('Informe seu ano de nascimento: '))
if ano_atual - ano_nasc <= 9:
    print('O Atleta tem {}{} anos{}, pertence a categoria {}"MIRIM"{}'
          .format(color['purple'], ano_atual - ano_nasc, color['clear'], color['purple'], color['clear']))
elif ano_atual - ano_nasc <= 14:
    print('O Atleta tem {}{} anos{}, pertence a categoria {}"INFANTIL"{}'
          .format(color['green'], ano_atual - ano_nasc, color['clear'], color['green'], color['clear']))
elif ano_atual - ano_nasc <= 19:
    print('O Atleta tem {}{} anos{}, pertence a categoria {}"JUNIOR"{}'
          .format(color['yellow'], ano_atual - ano_nasc, color['clear'], color['yellow'], color['clear']))
elif ano_atual - ano_nasc <= 25:
    print('O Atleta tem {}{} anos{}, pertence a categoria {}"SÊNIOR"{}'
          .format(color['cyan'], ano_atual - ano_nasc, color['clear'], color['cyan'], color['clear']))
else:
    print('O Atleta tem {}{} anos{}, pertence a categoria {}"MASTER"{}'
          .format(color['red'], ano_atual - ano_nasc, color['clear'], color['red'], color['clear']))
