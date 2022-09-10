from math import hypot
oposto = float(input('Qual o cateto oposto?'))
adjacente = float(input('Qual o cateto adjacente?'))
hipotenusa = hypot(oposto, adjacente)
print(f'a hipotenusa é {hipotenusa:.2f}')
