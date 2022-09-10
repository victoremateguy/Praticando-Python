fim = 0
escolha = 0
while escolha != 5:
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo valor: '))
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('>>>>>>> Qual é a sua opção? '))
    if escolha == 1:
        print(f'A soma entre {valor1} + {valor2} é {valor1 + valor2}')
    elif escolha == 2:
        print(f'{valor1} X {valor2} é {valor1 * valor2}')
    elif escolha == 3:
        if valor1 > valor2:
            print(f'{valor1} é maior que {valor2}')
        elif valor2 > valor1:
            print(f'{valor2} é maior que {valor1}')
        else:
            print('Os dois números são iguais.')
    else:
        print('Opção inválida. Tente novamente!')
    print('-=' * 20)

print('Fim. Volte sempre!')