km = float(input('Qual foi a distancia percorrida? '))
if km <= 200:
    v1 = km * 0.50
    print(f'Seu aluguel deu R${v1:.2f}')
else:
    v1 = km * 0.45
    print(f'Seu aluguel com desconto deu R${v1:.2f}')