n = s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma dos {cont} valores foi {s}')