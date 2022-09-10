cont = 1
num = int(input('Digite um número: '))
continua = str(input('Quer continuar? [S/N] ')).upper().strip()
maior = num
menor = num
media = num
media2 = 0
while continua != 'N':
    cont +=1
    num = int(input('Digite um número: '))
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()
    media2 = (media + num) / 2
    if maior < num:
        maior = num
    if menor > num:
        menor = num
print(f'Você digitou {cont} números e a média foi {media2}')
print(f'O maior valor foi {maior} e o menor foi {menor}')