dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos Km rodou com o carro? '))
v = (dias * 60) + (km * 0.15)
print(f'Você ficou {dias} dias com o carro e rodou {km:.1f}Km, Portanto deverá pagar R${v:.2f} pelo serviço.')
