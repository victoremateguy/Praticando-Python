v = int(input('Qual a velocidade do carro? '))
if v >= 80:
    print(f'Você foi multado e deverá pagar {(v - 80) * 7}')
else:
    print('Você está na velocidade permitida!')


