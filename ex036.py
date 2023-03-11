import emoji
print('APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO')
vl_imovel = float(input('Informe o valor do imóvel: R$ '))
salario = float(input('Informe o valor do seu salário: R$ '))
prazo = float(input('Informe em anos, o prazo de quitação: '))
parcelas = (vl_imovel / (prazo * 12))
teto = (100 / (salario / parcelas))
if teto > 30:
    print('''EMPRÉSTIMO NO VALOR DE R$ {:.2f}.
SERÃO {} PARCELAS NO VALOR DE R$ {:.2f}.
SEU SALÁRIO É DE R$ {:.2f}.
AS PARCELAS COMPROMETERÃO {:.2f}% DO SEU SALÁRIO. 
\033[1;31m=== SEU EMPRÉSTIMO FOI REJEITADO ===\033[m
Tente aumentar o prazo ou a quantidade de parcelas.
'''.format(vl_imovel, prazo * 12, parcelas, salario, teto))
else:
    print('''EMPRÉSTIMO NO VALOR DE R$ {:.2f}.
SERÃO {} PARCELAS NO VALOR DE R$ {:.2f}.
SEU SALÁRIO É DE R$ {:.2f}.
AS PARCELAS COMPROMETERÃO {:.2f}% DO SEU SALÁRIO.
\033[1;32mPARABÉNS, SEU EMPRÉSTIMO FOI APROVADO\033[m'''.format(vl_imovel, prazo * 12, parcelas, salario, teto))
print('Disponha sempre de nossos serviços.{}{}'.format(emoji.emojize(':grinning_face:'), emoji.emojize(':thumbs_up:')))
