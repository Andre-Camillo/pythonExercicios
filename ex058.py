from emoji import emojize
from random import randint
cont = 1
comp = randint(0, 10)
user = int(input('ESCOLHA UM NÚMERO ENTRE "0 E 10": '))
while comp != user:
    if comp > user:
        user = int(input('UM POUCO MAIS ACIMA: '))
    if comp < user:
        user = int(input('UM POUCO MAIS ABAIXO: '))
    if comp == user:
        print('PARABÉNS, VOCÊ ACERTOU!!! {}{}\nO NÚMERO ESCOLHI FOI O {}.'.format(emojize(":thumbs_up:"), emojize(":thumbs_up:"), comp))
    cont += 1
#if comp == user:
#    print('PARABÉNS, VOCÊ ACERTOU!!! {}{}'.format(emojize(":thumbs_up:"), emojize(":thumbs_up:")))
#else:
#    print('AHHH, QUE PENA!!! VOCÊ ERROU, TENTE NOCVAMENTE{}{}.'
#          .format(emojize(":sad_but_relieved_face:"), emojize(":sad_but_relieved_face:")))
print('FORAM AO TODO {} TENTATIVAS.'.format(cont))
print('FIM')
