print('Bem vindo ao Emateguy Financial!')
valor = float(input('Qual o valor da casa que deseja financiar? R$'))
salario = float(input('Qual o valor de seu salário mensal? R$'))
anos = int(input('Em quantos anos pretende financiar o imovel? '))
parcelas = (valor / anos) / 12
salario2 = salario * (30/100)
if salario2 <= parcelas:
    print(f'Infelizmente a parcela ficaria R${parcelas:.2f} por mês, e excederia 30% de seu salário.\n PEDIDO NEGADO!')
else:
    print(f'As parcelas são compativeis com sua renda, o valor ficará R${parcelas:.2f}. \n PEDIDO ACEITO!')