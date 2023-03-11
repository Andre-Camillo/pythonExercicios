som_idade = 0
media_idade = 0
maior_idade_hom = 0
nome_velho = ''
total_mul_20 = 0
for p in range(1, 5):
    print('----{}ª PESSOA -----'.format(p))
    nome = str(input('Nome: '.format(p)))
    idade = int(input('Idade: '.format(p)))
    sexo = str(input('Sexo [M/F]: '.format(p)))
    som_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_hom = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_hom:
        maior_idade_hom = idade
        nome_velho = nome
    if sexo == 'f'.lower() and  idade < 20:
        total_mul_20 += 1
media_idade = som_idade / 4
print('MÉDIA DE IDADE DO GRUPO É DE: "{}" ANOS.'.format(media_idade))
print('O HOMEM MAIS VELHO TEM "{}" ANOS E SE CHAMA: "{}".'.format(maior_idade_hom, nome_velho.upper()))
print('O GRUPO TEM "{}" MULHER(ES) ABAIXO DE 20 ANOS.'.format(total_mul_20))
