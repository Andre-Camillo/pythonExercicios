print('MÉTODO GUANABARA')
expr = str(input('DIGITE SUA EXPRESSÃO: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A EXPRESSÃO ESTÁ CORRETA.')
else:
    print('A EXPRESSÃO ESTÁ INCORRETA.')

print()

print('MEU MÉTODO')
exp = str(input('DIGITE SUA EXPRESSÃO: '))
cont_open = cont_close = 0

for c in exp:
    if c in '(':
        cont_open += 1
    if c in ')':
        cont_close += 1
if cont_open == cont_close:
    print('A EXPRESSÃO ESTÁ CORRETA.')
else:
    print('A EXPRESSÃO ESTÁ INCORRETA.')
