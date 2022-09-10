while True:
    cont = 0
    print('--'*20)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('--'*20)
    if valor < 0:
        break
    while cont <= 10:
        print(f'{valor} X {cont} = {valor * cont}')
        cont += 1
