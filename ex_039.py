from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
ano2 = nasc + 17
falta = ano2 - atual
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print(f'está na hora de se alistar!')
elif idade < 18:
    print(f'ainda falta(m) {falta} ano(s) para o alistamento.')
    ano3 = atual + falta
    print(f'seu alistamento será em {ano3}')
else:
    print(f'deveria ter se alistado em {ano2}')

