'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')'''


'''n = int(input('Digite um número para calcular seu Fatorial: ')) #meu jeito
r = n
i = n - 1
f = n - 1
while i != 0:
    r = f * r
    i -= 1
    f -= 1
print(f'O fatorial de {n} é {r}.')'''

n = int(input('Digite um número para ver o fatorial: '))
c = n
f = 1
print(f'Calculando {n}! =', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')