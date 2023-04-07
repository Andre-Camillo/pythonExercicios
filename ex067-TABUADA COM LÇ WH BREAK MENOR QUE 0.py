print('TABUADA COM LÇ WH BREAK < 0')
num = 0
while True:
    num = int(input('Digite um valor: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')


