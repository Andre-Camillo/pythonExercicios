import socket as s
host = input('INFORME O NOME DO HOST: ')
#EX: google.com
ip = s.gethostname(host)
print(f'O IP DO HOST {host} É: {ip}')
