print('DISSECA O VALOR')
algo = input('Digite algo: ')
print('Tipo primitivo: {}'.format(type(algo)))
print('É numérico? {}'.format(algo.isnumeric()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('É alfabético? {}'.format(algo.isalpha()))
print('Está em minúsculo? {}'.format(algo.islower()))
print('Está em maiúsculo? {}'.format(algo.isupper()))
print('Somente espaços? {}'.format(algo.isspace()))
print('Está Capitalizado? {}'.format(algo.istitle()))