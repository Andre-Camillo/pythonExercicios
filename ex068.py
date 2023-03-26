from random import randint
print('===== PAR OU IMPAR =====')
win = lose = 0
escolha = str(input('======== OPÇÕES ========\nESCOLHA "PAR" ou "IMPAR" [P] ou [I]": ')).strip().upper()
comput = randint(0, 9)
user = int(input('DIGITE UM NÚMERO: '))
result = comput + user
print(f'Computador escolheu: {comput}.\nVocê escolheu: {user}.\nTotal: {result}.')

if result % 2 == 1:
    clue = 'impar'
    print(f'{result} é IMPAR.')
else:
    clue = 'par'
    print(f'{result} é PAR.')

if escolha == 'P' and clue == 'par':
    win += 1
    print('Parabéns!! Você venceu.')
elif escolha == 'P' and clue == 'impar':
    lose += 1
    print('Tente novamente.')
elif escolha == 'I' and clue == 'impar':
    win += 1
    print('Parabéns!! Você venceu.')
elif escolha == 'I' and clue == 'par':
    lose += 1
    print('Tente novamente.')
print(f'Vitória(s): {win}\nDerrotas: {lose}')
