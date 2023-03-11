print('A CIDADE COMEÇA COM "SANTO"??')
cid = str(input('Em que cidade você nasceu? ')).strip().title()
print('É {} que {} começa com "Santo"'.format('santo' in cid.lower().split()[0], cid))


