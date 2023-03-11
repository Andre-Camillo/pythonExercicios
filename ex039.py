from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Informe o ano em que você nasceu: '))
if ano_atual - ano_nasc < 18:
    print('Você tem {} anos de idade, resta(m) {} ano(s) para se alistar.'.format(ano_atual - ano_nasc, 18 - (ano_atual - ano_nasc)))
elif ano_atual - ano_nasc == 18:
    print('Você tem {} anos de idade, está na hora de se alistar.'.format(ano_atual - ano_nasc))
elif ano_atual - ano_nasc > 18:
    print('Você tem {} anos de idade, deveria ter se alistado há {} anos.'.format(ano_atual - ano_nasc, (ano_atual - ano_nasc) - 18))