times = ('CORINTHIANS', 'SANTOS', 'SÃO PAULO', 'PALMEIRAS', 'FLAMENGO', 'FLUMINENSE', 'BOTA FOGO', 'VASCO', 'ATLETICO MG', 'CRUZEIRO'
         , 'GRÊMIO', 'INTER', 'FORTALEZA', 'CEARÁ', 'GOIÁS', 'RB BRAGANTINO', 'CORITIBA', 'ATLETICH', 'BAHIA', 'CUIABÁ')
print('\033[1:36mDO 1º AO 5º COLOCADO:\033[m ')
for c in range(0, len(times[0:5])):
    print(f'{c + 1}º {times[c]}')

print('\033[1:36m\nOS ÚLTIMOS 4 COLOCADOS: \033[m')
for c in range(16, len(times)):
    print(f'{c + 1}º {times[c]}')

print('\033[1:36m\nEM ORDEM ALFABÉTICA:\033[m')
for pos, c in enumerate(sorted(times)):
    print(f'{pos + 1}º {c}')

nome = str(input('\033[1:36m\nINFORME O NOME DA EQUIPE PARA SABER SEU POSICINOAMENTO NA TABELA: \033[m')).upper()

print(f'{nome} ESTÁ NA POSIÇÃO Nº {times.index(nome) + 1}')

