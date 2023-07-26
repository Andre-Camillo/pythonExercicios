exp = str(input('DIGITE SUA EXPRESSÃO: '))
cont_open = cont_close = 0
for c in exp:
    if c in '(':
        cont_open += 1
    if c in ')':
        cont_close += 1
if cont_open == cont_close:
    print('SUA EXPRESSÃO ESTÁ CORRETA.')
else:
    print('SUA EXPRESSÃO ESTÁ INCORRETA.')


