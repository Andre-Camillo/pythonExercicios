from random import randint
from emoji import emojize
color = {"clear": "\033[m", "red": "\033[1;31m", "green": "\033[1;32m", "cyan": "\033[1;36m", "purple": "\033[1;35m", "<B>": "\033[1m"}
print('========== PAR OU IMPAR ==========\n')
nome = str(input('INFORME SEU NOME: ')).strip().upper()
win = 0
while True:
    comput = randint(0, 10)
    escolha = str(input('ESCOLHA "PAR" ou "IMPAR" [P] ou [I]": ')).strip()
    while escolha not in 'PpIi':
        escolha = str(input('VOCÊ DEVE ESCOLHER "PAR" ou "IMPAR" [P] ou [I]": ')).strip()
    user = int(input('DIGITE UM NÚMERO: '))
    result = comput + user
    print(f'\nComputador escolheu: {comput}.\nVocê escolheu: {user}.\nTotal: {result}.\n')
    if result % 2 == 1:
        aposta = 'impar'
        print(f'{result} é IMPAR.')
    else:
        aposta = 'par'
        print(f'{result} é PAR.')
    if escolha in 'Pp' and aposta == 'par':
        win += 1
        print(f'{color["cyan"]}CONGRATULATIONS!!{color["clear"]} {color["<B>"]}{nome}{color["clear"]}.\n{color["green"]}YOU WIN{color["clear"]}{emojize(":thumbs_up:")}')
        print('=' * 35)
        print('')
    elif escolha in 'Pp' and aposta == 'impar':
        print(f'{color["purple"]}SORRY{color["clear"]} {color["<B>"]}{nome}{color["clear"]}.'
              f'\n{color["red"]}YOU LOOSE{color["clear"]}{emojize(":thumbs_down:")}')
        break
    elif escolha in 'Ii' and aposta == 'impar':
        win += 1
        print(f'{color["cyan"]}CONGRATULATIONS!!{color["clear"]} {color["<B>"]}{nome}{color["clear"]}.\n{color["green"]}YOU WIN{color["clear"]}{emojize(":thumbs_up:")}')
        print('=' * 35)
        print('')
    elif escolha in 'Ii' and aposta == 'par':
        print(f'{color["purple"]}SORRY{color["clear"]} {color["<B>"]}{nome}{color["clear"]}.'
              f'\n{color["red"]}YOU LOOSE{color["clear"]}{emojize(":thumbs_down:")}')
        break
print(f'Total de: {win} Vitória(s).')
print('=' * 35)
