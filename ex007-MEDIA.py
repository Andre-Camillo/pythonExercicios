print('MEDIA')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if n1 > n2:
    print('A nota mais alta foi: {:.1f}'.format(n1))
    print('A nota mais baixa foi: {:.1f}'.format(n2))
elif n2 > n1:
    print('A nota mais alta foi: {:.1f}'.format(n2))
    print('A nota mais baixa foi: {:.1f}'.format(n1))
print('Sua media aritmetica é: {:.1f}'.format((n1 + n2) / 2))
