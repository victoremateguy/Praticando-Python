from random import randint, random
from time import sleep
n = randint(0, 5) #faz o computador pensar num numero
print('Vamos brincar de adivinhação?')
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. tente advinhar...')
print('-=-' *20)
n1 = int(input('Qual número de 0 a 5 estou pensando? ')) #jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
while n1 != n:
    print(f'Você errou. Tente novamente!')
    n1 = int(input('Qual número de 0 a 5 estou pensando? '))
print(f'Parabéns! eu pensei no número {n}!')

'''computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou! com {palpites} tentativas')'''
