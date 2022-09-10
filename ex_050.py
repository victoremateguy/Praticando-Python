cont = 0
s = 0
for c in range(1, 7):
    v = int(input('Digite um número: '))
    if v % 2 == 0:
        s += v
        cont += 1
print(f'A soma dos {cont} números deu {s}')