print('RADAR')
veloc = float(input('Informe a velocidade do veículo: '))
vl_multa = float(input('Informe o valor por km excedente: R$ '))
if veloc > 80:
    print('''Você está trafegando a {} km/h.
{} km/h a cima do limite permitido - (80 km/h).
Valor da multa R$ {:.2f}'''.format(veloc, veloc - 80, (veloc - 80) * vl_multa))


