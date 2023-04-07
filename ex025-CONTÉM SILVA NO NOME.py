print('CONTÉM "SILVA" NO NOME:')
nome = str(input('Digite seu nome completo: ')).strip()
print('É {} que no nome {} contém o nome "Silva".'.format('silva' in nome.lower(), ' '.join(nome.title().split())))

