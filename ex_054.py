from datetime import date

menor = 0
maior = 0
atual = date.today().year

for c in range(1, 8):
    idade = int(input(f'Em que ano a {c}ᵃ pessoa nasceu? '))
    if idade >= atual - 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade\n E também tivemos {menor} pessoas menores de idade.')