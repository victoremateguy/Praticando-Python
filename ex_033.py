a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando menor
menor = a
if b < a and b < c:
        menor = b
if c < a and c < b:
    menor = c
#verificando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'o menor valor digitado foi {menor} e o maior foi {maior}')
