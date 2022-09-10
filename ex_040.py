n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
soma = (n1 + n2 + n3) / 3
if 5.0 <= soma < 7:
    print('Parabéns! você está de RECUPERAÇÃO, seu trouxa!')
elif soma < 5.0:
    print('Como você consegue ser tão ruim??? REPROVADO!!!')
elif soma >= 7:
    print('Não fez mais que a sua obrigação. Você está APROVADO.')