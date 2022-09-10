soma = cont = menor = nomemenor = 0

print('--'*20)
print('LOJA SUPER DO VITÃO')
nome = str(input('Nome do produto: '))
preco = float(input('Preço: R$'))
while True:
    soma += preco
    if preco > 1000:
        cont += 1
    if menor > preco:
        menor = preco
        nomemenor = nome
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
        while continua != 'S':
                break
    print('--'*20)
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi')


