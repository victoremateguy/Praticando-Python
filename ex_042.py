print('-='*20)
print('Analisador de triangulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os segmentos podem formar um triangulo EQUILATERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Os segmentos podem formar um triangulo ISOSCELES')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Os segmentos podem formar um triangulo ESCALENO')
else:
    print(f'Os segmentos acima não podem formar um triangulo.')