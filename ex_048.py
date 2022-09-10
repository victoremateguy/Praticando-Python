cont = 0
s = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n
        cont += 1
print(f'\nA soma de todos os {cont} valores impares deu {s}')