print('JOGO DE ADIVINHA')
import emoji
from random import randint
num = int(input('Escolha um número entre 0 e 5: '))
pc = randint(0, 5)
print('Você escolheu  número: {}'.format(num))
print('O Computador escolheu o número: {}'.format(pc))
if pc == num:
    print('Parabéns! Você venceu. {}'.format(emoji.emojize(':thumbs_up:')))
else:
    print('Não foi desta vez. {}'.format(emoji.emojize(':thumbs_down:')))
