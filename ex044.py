print('GERENCIADOR DE PAGAMENTOS')
valor = float(input('INFORME O VALOR DO PRODUTO: R$ '))
formas = int(input('''FORMAS DE PAGAMENTO:
[ 1 ] À VISTA EM DINHEIRO OU CHEQUE - (10 % DESCONTO)
[ 2 ] À VISTA NO CARTÃO - (5% DESCONTO) 
[ 3 ] ATÉ 2 VEZES NO CARTÃO - (VALOR DE PRATELEIRA) 
[ 4 ] 3 VEZES OU MAIS NO CARTÃO - (ATÉ 20% DE JUROS)
ESCOLHA A FORMA DE PAGAMENTO: '''))
print('-=' * 20)
if formas == 1:
    print('''FORMA DE PAGAMENTO: À VISTA - (DINHEIRO OU CHEQUE)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO COM 10% DE DESCONTO: R$ {:.2f}\033[m.'''.format(valor, valor - valor * 10 / 100))
elif formas == 2:
    print('''FORMA DE PAGAMENTO: À VISTA - (NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO COM 5% DE DESCONTO: R$ {:.2f}\033[m.'''.format(valor, valor - valor * 5 / 100))
elif formas == 3:
    quant = int(input('''QUANTIDADE DE PARCELAS
[ 1 ] PARA 1 VEZ NO CARTÃO.
[ 2 ] PARA 2 VEZES NO CARTÃO.
INFORME A QUANTIDADE DE PARCELAS: '''))
    if quant == 1:
        print('''FORMA DE PARCELAMENTO: (1 VEZ NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (1 VEZ NO CARTÃO): R$ {:.2f}\033[m.'''.format(valor, valor + valor * 1 / 100))
    elif quant == 2:
        print('''FORMA DE PARCELAMENTO: (2 VEZES NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (2 VEZES NO CARTÃO): R$ {:.2f}\033[m.
SERÃO 2 PARCELAS DE R$ {:.2f} CADA.'''.format(valor, valor + valor * 2 / 100, (valor + valor * 2 / 100) / 2))
elif formas == 4:
    quant = int(input('''QUANTIDADE DE PARCELAS
[ 1 ] PARA 1 VEZ NO CARTÃO.
[ 2 ] PARA 2 VEZES NO CARTÃO.
[ 3 ] PARA 3 VEZES NO CARTÃO.
[ 4 ] PARA 4 VEZES NO CARTÃO.
[ 5 ] PARA 5 VEZES NO CARTÃO.
[ 6 ] PARA 6 VEZES NO CARTÃO.
[ 7 ] PARA 7 VEZES NO CARTÃO.
[ 8 ] PARA 8 VEZES NO CARTÃO.
INFORME A QUANTIDADE DE PARCELAS: '''))
    if quant == 1:
        print('''FORMA DE PARCELAMENTO: (1 VEZ NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (1 VEZ NO CARTÃO): R$ {:.2f}\033[m.'''.format(valor, valor + valor * 2.5 / 100))
    elif quant == 2:
        print('''FORMA DE PARCELAMENTO: (2 VEZES NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (2 VEZES NO CARTÃO): R$ {:.2f}\033[m.
\033[1;33mSERÃO 2 PARCELAS DE R$ {:.2f}\033[m.'''.format(valor, valor + valor * 5 / 100, (valor + valor * 5 / 100) / 2))
    elif quant == 3:
        print('''FORMA DE PARCELAMENTO: (3 VEZES NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (3 VEZES NO CARTÃO): R$ {:.2f}\033[m.
\033[1;33mSERÃO 3 PARCELAS DE R$ {:.2f}\033[m.'''.format(valor, valor + valor * 7.5 / 100, (valor + valor * 7.5 / 100) / 3))
    elif quant == 4:
        print('''FORMA DE PARCELAMENTO: (4 VEZES NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (4 VEZES NO CARTÃO): R$ {:.2f}\033[m.
\033[1;33mSERÃO 4 PARCELAS DE R$ {:.2f}\033[m.'''.format(valor, valor + valor * 10 / 100, (valor + valor * 10 / 100) / 4))
    elif quant == 5:
        print('''FORMA DE PARCELAMENTO: (5 VEZES NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (5 VEZES NO CARTÃO): R$ {:.2f}\033[m.
\033[1;33mSERÃO 5 PARCELAS DE R$ {:.2f}\033[m.'''.format(valor, valor + valor * 12.5 / 100, (valor + valor * 12.5 / 100) / 5))
    elif quant == 6:
        print('''FORMA DE PARCELAMENTO: (6 VEZES NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (6 VEZES NO CARTÃO): R$ {:.2f}\033[m.
\033[1;33mSERÃO 6 PARCELAS DE R$ {:.2f}.\033[m'''.format(valor, valor + valor * 15 / 100, (valor + valor * 15 / 100) / 6))
    elif quant == 7:
        print('''FORMA DE PARCELAMENTO: (7 VEZES NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (7 VEZES NO CARTÃO): R$ {:.2f}\033[m.
\033[1;33mSERÃO 7 PARCELAS DE R$ {:.2f}\033[m.'''.format(valor, valor + valor * 17.5 / 100, (valor + valor * 17.5 / 100) / 7))
    elif quant == 8:
        print('''FORMA DE PARCELAMENTO: (8 VEZES NO CARTÃO)
\033[1;36mVALOR ATUAL DO PRODUTO: R$ {:.2f}\033[m.
\033[1;32mVALOR DO PRODUTO (8 VEZES NO CARTÃO): R$ {:.2f}\033[m.
\033[1;33mSERÃO 8 PARCELAS DE R$ {:.2f}\033[m.'''.format(valor, valor + valor * 20 / 100, (valor + valor * 20 / 100) / 8))
