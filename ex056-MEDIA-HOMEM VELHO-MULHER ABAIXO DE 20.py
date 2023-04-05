print('MEDIA-HOMEM VELHO-MULHER ABAIXO DE 20')
cont_idade = 0
nomeMaisVelho = ''
maiorIdadeHomem = 0
mulher = 0
for c in range(1, 5):
    nome = str(input('INFORME O NOME DA {}ª PESSOA: '.format(c)))
    idade = int(input('INFORME A IDADE DA {}ª PESOOA: '.format(c)))
    sexo = str(input('INOFRME O SEXO DA {}ª PESSOA [M] ou [F]: '.format(c)))
    print('=' * 45)
    cont_idade += idade
    if c == 1 and sexo in "Mm":
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in "Mm" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in "Ff" and idade < 20:
        mulher += 1
print('A media de idade do grupo é de: {} anos.'.format(cont_idade / 4))
print('O homem mais velho tem {} anos e chama-se: {}'.format(maiorIdadeHomem, nomeMaisVelho))
print('Ao todo temos {} mulher(es) abaixo de 20 anos'.format(mulher))
