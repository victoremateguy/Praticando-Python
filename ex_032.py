from datetime import date
ano = int(input('Que ano quer analisar? digite 0 para analisar o ano atual: '))
resultado = ano % 4
if ano == 0:
    ano = date.today().year
if resultado == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é bissexto!')
else:
    print(f'o ano {ano} não é bissexto :(')