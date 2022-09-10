velho = 0
mulheres = 0
media = 0.0
cont = 0
while True:
    sexo = ''
    continua = ''
    cont += 1
    print(f'----- {cont}ᵃ PESSOA -----')
    idade = float(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F]')).strip().upper()
    media += idade
    if sexo == 'M' and idade > velho:
        velho = idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
    while continua != 'S' and continua != 'N':
        continua = str(input('Você quer continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break
media = media / cont
print(f'A média de idade do grupo é de {media:.1f} anos.')
velho = int(velho)
print(f'O homem mais velho tem {velho} anos.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos.')