from random import randint
from time import sleep
contjogador = jogador = escolha = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('-=' * 20)
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    pc = randint(0, 10)
    soma = jogador + pc
    resultado = (jogador + pc) % 2
    if escolha == 'P':
        if resultado == 0:
            print('--' * 20)
            print(f' você jogou {jogador} e o computador {pc}. Total de {soma} DEU PAR')
            print('--' * 20)
            print('Você venceu')
            print('Vamos jogar novamente...')
            sleep(1)
            contjogador += 1
        else:
            print('--' * 20)
            print(f'você jogou {jogador} e o computador {pc}. Total de {soma} DEU IMPAR')
            print('--' * 20)
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if resultado == 0:
            print('--' * 20)
            print(f' você jogou {jogador} e o computador {pc}. Total de {soma} DEU PAR')
            print('--' * 20)
            print('Você perdeu!')
            break
        else:
            print('--' * 20)
            print(f' você jogou {jogador} e o computador {pc}. Total de {soma} DEU IMPAR')
            print('--' * 20)
            print('Você ganhou!')
            print('Vamos jogar novamente...')
            sleep(1)
            contjogador += 1
print('-=' * 20)
print(f'GAME OVER! Você venceu {contjogador} vezes.')