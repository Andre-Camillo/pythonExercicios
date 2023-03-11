from emoji import emojize
from time import sleep
from random import randint
comp = randint(1, 3)
vc = int(input('''*** OPÇÕES DE ESCOLHA ***
\033[1;37m[ 1 ] PEDRA\033[m
\033[1;35m[ 2 ] PAPEL\033[m
\033[1;36m[ 3 ] TESOURA\033[m
ESCOLHA UMA DAS OPÇÕES: '''))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
if comp == 1 and vc == 1:
    print('COMPUTADOR ESCOLHEU: \033[1;37mPEDRA\033[m\nVOCÊ ESCOLHEU: \033[1;37mPEDRA\033[m\n\033[1;33mEMPATOU{}\033[m'
          .format(emojize(':neutral_face:')))
elif comp == 1 and vc == 2:
    print('COMPUTADOR ESCOLHEU: \033[1;37mPEDRA\033[m\nVOCÊ ESCOLHEU: \033[1;35mPAPEL\033[m\n\033[1;32mVOCÊ VENCEU{}\033[m'
          .format(emojize(':grinning_face_with_big_eyes:')))
elif comp == 1 and vc == 3:
    print('COMPUTADOR ESCOLHEU: \033[1;37mPEDRA\033[m\nVOCÊ ESCOLHEU: \033[1;36mTESOURA\033[m\n\033[1;31mVOCÊ PERDEU{}\033[m'
          .format(emojize(':pleading_face:')))
elif comp == 2 and vc == 1:
    print('COMPUTADOR ESCOLHEU: \033[1;35mPAPEL\033[m\nVOCÊ ESCOLHEU: \033[1;37mPEDRA\033[m\n\033[1;31mVOCÊ PERDEU{}\033[m'
          .format(emojize(':pleading_face:')))
elif comp == 2 and vc == 2:
    print('COMPUTADOR ESCOLHEU: \033[1;35mPAPEL\033[m\nVOCÊ ESCOLHEU: \033[1;35mPAPEL\033[m\n\033[1;33mEMPATOU{}\033[m'
          .format(emojize(':neutral_face:')))
elif comp == 2 and vc == 3:
    print('COMPUTADOR ESCOLHEU: \033[1;35mPAPEL\033[m\nVOCÊ ESCOLHEU: \033[1;36mTESOURA\033[m\n\033[1;32mVOCÊ VENCEU{}\033[m'
          .format(emojize(':grinning_face_with_big_eyes:')))
elif comp == 3 and vc == 1:
    print('COMPUTADOR ESCOLHEU: \033[1;36mTESOURA\033[m\nVOCÊ ESCOLHEU: \033[1;37mPEDRA\033[m\n\033[1;32mVOCÊ VENCEU{}\033[m'
          .format(emojize(':grinning_face_with_big_eyes:')))
elif comp == 3 and vc == 2:
    print('COMPUTADOR ESCOLHEU: \033[1;36mTESOURA\033[m\nVOCÊ ESCOLHEU: \033[1;35mPAPEL\033[m\n\033[1;31mVOCÊ PERDEU{}\033[m'
          .format(emojize(':pleading_face:')))
elif comp == 3 and vc == 3:
    print('COMPUTADOR ESCOLHEU: \033[1;36mTESOURA\033[m\nVOCÊ ESCOLHEU: \033[1;36mTESOURA\033[m\n\033[1;33mEMPATOU{}\033[m'
          .format(emojize(':neutral_face:')))
else:
    print('\033[1mVOCÊ DEVE ESCOLHER UMA DAS OPÇÕES\033[m\n'
'\033[1;37m[ 1 ] PEDRA\033[m\n\033[1;35m[ 2 ] PAPEL\033[m\n\033[1;36m[ 3 ] TESOURA\033[m\n\033[1mVOCÊ DIGITOU: {} - OPÇÃO INEXISTENTE.\n'
'POR FAVOR TENTE NOVAMENTE\033[m.'.format(vc))
