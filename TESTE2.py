mai = men = 0
for c in range(1, 4):
    kilos = float(input(f'INFORME O PESO DA {c}ª PESSOA: '))
    if c == 1:
        mai = men = kilos
    else:
        if kilos > mai:
            mai = kilos
        if kilos < men :
            men = kilos
print(f'O MAIS PESADO: {mai}.\nO MAIS LEVE: {men}.')



