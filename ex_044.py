print('EMATEGUY STORE')

valor = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input('Qual é a opção? '))
if escolha == 1:
    desconto = valor * (10 / 100)
    final = valor - desconto
    print(f'O valor à vista deu R${final:.2f}.')
elif escolha == 2:
    desconto = valor * (5 / 100)
    final = valor - desconto
    print(f'O valor à vista no cartão deu R${final:.2f}.')
elif escolha == 3:
    parcela = valor / 2
    print(f'O valor é R${valor:.2f}, portanto a parcela ficará R${parcela:.2f} em 2 vezes.')
elif escolha == 4:
    parcela = int(input('Qual o número de parcelas? '))
    if parcela < 3:
        print('ENTRADA INVALIDA!')
    else:
        juros = valor * (20 / 100)
        final = valor + juros
        parcela2 = valor / parcela
        print(f'O valor total com juros deu R${final:.2f}. \n Você pagará R${parcela2:.2f} em {parcela} parcelas.')
