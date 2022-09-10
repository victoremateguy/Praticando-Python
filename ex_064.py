num = 0
resultado = 0
cont = -1
while num != 999:
    resultado += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'A soma entre os {cont} números deu {resultado}')
print('Acabou.')