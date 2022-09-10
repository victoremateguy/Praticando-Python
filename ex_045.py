from random import randint
from time import sleep
print('''Vamos jogar JO-KEN-PO?
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escolha = int(input('Qual é sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
pc = randint(0, 2)
if escolha == 0 and pc == 0:
    print(f'''Eu tirei PEDRA e você TAMBÉM
    EMPATAMOS!!!''')
elif escolha == 1 and pc == 1:
    print(f'''Eu tirei PAPEL e você TAMBÉM
    EMPATAMOS!!!''')
elif escolha == 2 and pc == 2:
    print('''Eu tirei TESOURA e você TAMBÉM
    EMPATAMOS!!!''')
elif escolha == 0 and pc == 1:
    print('''Eu tirei PAPEL e você PEDRA
    Eu ganhei!''')
elif escolha == 0 and pc == 2:
    print('''Eu tirei TESOURA e você PEDRA
    Você ganhou!''')
elif escolha == 1 and pc == 0:
    print('''Eu tirei PEDRA e você PAPEL
    Você ganhou!''')
elif escolha == 1 and pc == 2:
    print('''Eu tirei TESOURA e você PAPEL
    Eu ganhei!''')
elif escolha == 2 and pc == 0:
    print('''Eu tirei PEDRA e você TESOURA
    Eu ganhei!''')
elif escolha == 2 and pc == 1:
    print('''Eu tirei PAPEL e você TESOURA
    Você ganhou!''')
else:
    print('Entrada invalida: TENTE NOVAMENTE.')
