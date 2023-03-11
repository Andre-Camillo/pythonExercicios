print('DETECTOR DE PALÍNDROMO')
colors = {'clean': '\033[m', 'red': '\033[1;31m', 'green': '\033[1;32m', 'cyan': '\033[1;36m'}
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverter = junto[:: -1]
#print(junto)
#print(inverter)
if junto == inverter:
    print('A frase \033[1m"{}{}{}"\033[m {}É UM PALÍNDROMO{}'.format(colors['cyan'], frase, colors['clean'], colors['green'], colors['clean']))
else:
    print('A frase \033[1m"{}{}{}"\033[m {}NÃO É UM PALÍNDROMO{}.'
          .format(colors['cyan'], frase, colors['clean'], colors['red'], colors['clean']))
