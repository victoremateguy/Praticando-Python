velho = 0
mulheres = 0
nome2 = ''
media = 0.0

for c in range(1, 5):
    print(f'----- {c}ᵃ PESSOA -----')
    nome = input('Nome: ').strip()
    idade = float(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    media += idade
    if sexo == 'M' and idade > velho:
        velho = idade
        nome2 = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
media = media / 4
print(f'A média de idade do grupo é de {media:.1f} anos.')
velho = int(velho)
print(f'O homem mais velho tem {velho} anos e se chama {nome2}.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos.')