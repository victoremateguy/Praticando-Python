from datetime import date

ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print(f'O atleta tem {idade} anos. \n Classificação: MIRIM')
elif 14 >= idade > 9:
    print(f'O atleta tem {idade} anos. \n Classificação: INFANTIL')
elif 19 >= idade > 14:
    print(f'O atleta tem {idade} anos. \n Classificação: JUNIOR')
elif 24 >= idade > 19:
    print(f'O atleta tem {idade} anos. \n Classificação: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos. \n Classificação: MASTER')