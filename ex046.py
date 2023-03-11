from emoji import emojize
from time import sleep
print('CONTAGEM REGERESSIVA')
for c in range(10, 0, -1):
    sleep(.5)
    print(c, end=' ')
sleep(.5)
print('{}'.format(emojize(':collision:')))


