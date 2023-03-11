peso = float(input('Informe o seu peso: '))
alt = float(input('Informe a sua altura: '))
imc = peso / alt ** 2
if imc < 18.5:
    print('\033[1;36mSEU IMC É: {:.2F}\033[m\nVocê está \033[1;34mABAIXO DO PESO\033[m.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('\033[1;36mSEU IMC É {:.2F}\033[m\nVocê está no \033[1;32mPESO IDEAL\033[m.'.format(imc))
elif imc >= 25 and imc < 30:
    print('\033[1;36mSEU IMC É: {:.2F}\033[m\nVocê está com \033[1;33mSOBREPESO\033[m.'.format(imc))
elif imc >= 30 and imc < 40:
    print('\033[1;36mSEU IMC É: {:.2F}\033[m\nVocê está \033[1;35mOBESO(A)\033[m.'.format(imc))
else:
    print('\033[1;36mSEU IMC É: {:.2F}\033[m\nVocê está \033[1;31mOBESIDADE MÓRBIDA(A)\033[m.'.format(imc))