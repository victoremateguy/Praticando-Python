print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} >>> ', end='')
    cont += 1
    termo += razao
print('PAUSA')
termo2 = termo
razao2 = 1
cont2 = cont
while razao2 != 0:
    razao2 = int(input('Quantos termos você quer mostrar a mais? '))
    while cont2 < cont + razao2:
        cont2 += 1
        termo2 += razao
        print(f'{termo2} >>> ', end='')
    print('PAUSA')
print('FIM')