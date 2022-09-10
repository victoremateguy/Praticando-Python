import random
from time import sleep
n = random.randint(0, 5) #faz o computador pensar num numero
print('Vamos brincar de adivinhação?')
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. tente advinhar...')
print('-=-' *20)
n1 = int(input('Qual número de 0 a 5 estou pensando? ')) #jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if n == n1:
    print(f'Parabéns! eu pensei no número {n}!')
else:
    print(f'Que pena, eu estava pensando em {n}!')

