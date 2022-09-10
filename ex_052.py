num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisivel {tot} vezes.')
if tot == 2:
    print(f'O número {num} é \033[34mprimo\033[m!')
else:
    print(f'O número {num} \033[31mnão\033[m é \033[31mprimo\033[m!')