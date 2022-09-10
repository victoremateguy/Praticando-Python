from math import radians, sin, cos, tan
graus = float(input('Diga a medida em graus:'))
radiando = radians(graus)
print(f'O seno é {sin(radiando):.2f}, cosseno é {cos(radiando):.2f} e tangente é {tan(radiando):.2f}')