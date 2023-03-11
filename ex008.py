print('CONVERSOR MÉTRICO')
num = float(input('Informe a metragem a ser convertida: '))
mm = num * 1000
cm = num * 100
dm = num * 10
dam = num / 10
hm = num / 100
km = num / 1000
print('''Convertendo {}m para mm: {}mm.
Convertendo {}m para cm: {}cm.
Convertendo {}m para dm: {}dm.
Convertendo {}m para dam: {}dam.
Convertendo {}m para hm: {}hm.
Convertendo {}m para km: {}km.'''.format(num, mm, num, cm, num, dm, num, dam, num, hm, num, km))
