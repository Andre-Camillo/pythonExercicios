from datetime import date
contIdade = contHomem = mulher20 = 0
#idade = sexo = ''
escolha = str(input('Poderia colaborar com nossa pesquisa? [S] ou [N]: ')).strip()
while escolha not in 'Nn':
    escolha = str(input('Você deve escolher: [S] ou [N]: ')).strip()
while escolha not in 'Nn':
    ano_nasc = int(input('Informe o ano em que você nasceu: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    sexo = str(input('Qual o seu sexo [M] ou [F]: ')).strip()
    escolha = str(input('Deseja Continuar? [S] ou [N]: '))
    while escolha not in 'SsNn':
        escolha = str(input('Você deve escolher: [S] ou [N]: ')).strip()
    if idade > 18:
        contIdade += 1
    if sexo[0] in 'Mm':
        contHomem += 1
    if sexo[0] in 'Ff' and idade < 20:
        mulher20 += 1
print(f'{contIdade} pessoa(s) tem mais de 18 anos.\n{contHomem} pessoa(s) (é)são do sexo Masculino\n{mulher20} mulher(es) tem menos de 20 anos.')
